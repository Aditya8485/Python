#!/usr/bin/env python3
"""
LineForge Splitter
Split large text files into smaller numbered files without loading everything into memory.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path


APP_NAME = "LineForge"
VERSION = "1.0"


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def banner() -> None:
    print("=" * 58)
    print(f"{APP_NAME} v{VERSION}".center(58))
    print("Fast line-based file splitter".center(58))
    print("=" * 58)


def clean_input(value: str) -> str:
    return value.strip().strip('"').strip("'")


def ask_file() -> Path:
    while True:
        raw = clean_input(input("\nEnter file path: "))
        if not raw:
            print("[!] File path cannot be empty.")
            continue

        path = Path(raw).expanduser()

        if not path.exists():
            print("[!] File not found. Check the path and try again.")
            continue

        if not path.is_file():
            print("[!] The given path is not a file.")
            continue

        return path.resolve()


def ask_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip().replace(",", "")
        try:
            value = int(raw)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("[!] Enter a whole number greater than 0.")


def ask_output_folder(source: Path) -> Path:
    default_folder = source.parent / f"{source.stem}_split"

    raw = clean_input(
        input(f"Output folder [{default_folder.name}]: ")
    )

    folder = Path(raw).expanduser() if raw else default_folder

    if not folder.is_absolute():
        folder = source.parent / folder

    folder.mkdir(parents=True, exist_ok=True)
    return folder.resolve()


def detect_encoding(path: Path) -> str:
    candidates = ("utf-8-sig", "utf-8", "cp1252", "latin-1")

    for encoding in candidates:
        try:
            with path.open("r", encoding=encoding) as file:
                for _ in range(100):
                    if not file.readline():
                        break
            return encoding
        except UnicodeDecodeError:
            continue

    return "latin-1"


def make_part_path(
    output_dir: Path,
    source: Path,
    part_number: int,
    width: int,
) -> Path:
    suffix = source.suffix or ".txt"
    base_name = source.stem if source.suffix else source.name
    return output_dir / f"{base_name}_part_{part_number:0{width}d}{suffix}"


def split_file(
    source: Path,
    output_dir: Path,
    lines_per_file: int,
    encoding: str,
) -> tuple[int, int]:
    total_lines = 0
    total_parts = 0
    output_file = None
    output_path = None
    started = time.perf_counter()

    try:
        with source.open("r", encoding=encoding, errors="replace", newline="") as input_file:
            for line_number, line in enumerate(input_file, start=1):
                if (line_number - 1) % lines_per_file == 0:
                    if output_file:
                        output_file.close()

                    total_parts += 1
                    output_path = make_part_path(
                        output_dir,
                        source,
                        total_parts,
                        width=4,
                    )
                    output_file = output_path.open(
                        "w",
                        encoding="utf-8",
                        newline="",
                    )

                output_file.write(line)
                total_lines = line_number

                if line_number % 100_000 == 0:
                    elapsed = max(time.perf_counter() - started, 0.001)
                    speed = int(line_number / elapsed)
                    print(
                        f"\r[>] Processed {line_number:,} lines "
                        f"| {speed:,} lines/sec",
                        end="",
                        flush=True,
                    )

        if output_file:
            output_file.close()

    except Exception:
        if output_file and not output_file.closed:
            output_file.close()

        if output_path and output_path.exists() and output_path.stat().st_size == 0:
            output_path.unlink(missing_ok=True)

        raise

    print("\r" + " " * 70 + "\r", end="")
    return total_lines, total_parts


def main() -> None:
    clear_screen()
    banner()

    source = ask_file()
    lines_per_file = ask_positive_int("Lines per output file: ")
    output_dir = ask_output_folder(source)
    encoding = detect_encoding(source)

    print("\n" + "-" * 58)
    print(f"Source       : {source}")
    print(f"Encoding     : {encoding}")
    print(f"Lines/part   : {lines_per_file:,}")
    print(f"Output       : {output_dir}")
    print("-" * 58)

    confirm = input("Start splitting? [Y/n]: ").strip().lower()
    if confirm not in ("", "y", "yes"):
        print("\nCancelled.")
        return

    print("\nSplitting started...\n")
    started = time.perf_counter()

    try:
        total_lines, total_parts = split_file(
            source=source,
            output_dir=output_dir,
            lines_per_file=lines_per_file,
            encoding=encoding,
        )
    except PermissionError:
        print("\n[ERROR] Permission denied. Close the file if it is open elsewhere.")
        sys.exit(1)
    except OSError as error:
        print(f"\n[ERROR] File operation failed: {error}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nStopped by user.")
        sys.exit(130)

    elapsed = time.perf_counter() - started

    print("\n" + "=" * 58)
    if total_lines == 0:
        print("The source file is empty. No output files were created.")
    else:
        print("Split completed successfully.")
        print(f"Total lines   : {total_lines:,}")
        print(f"Files created : {total_parts:,}")
        print(f"Time taken    : {elapsed:.2f} seconds")
        print(f"Saved in      : {output_dir}")
    print("=" * 58)

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
