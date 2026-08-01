from pathlib import Path

# Folder containing files to merge
MERGE_FOLDER = Path("merge")

# Output file
OUTPUT_FILE = Path("merged.txt")

# File extensions to include (empty = all files)
ALLOWED_EXTENSIONS = set()  # Example: {".txt", ".log"}

with OUTPUT_FILE.open("wb") as outfile:
    for file in sorted(MERGE_FOLDER.iterdir()):
        if not file.is_file():
            continue

        if ALLOWED_EXTENSIONS and file.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        print(f"Merging: {file.name}")

        with file.open("rb") as infile:
            outfile.write(infile.read())

print(f"\nDone! Output saved as: {OUTPUT_FILE}")