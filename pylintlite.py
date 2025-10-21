"""
PyLintLite 🧹
A minimal Python code linter for beginners.
Perfect for Hacktoberfest contributions!

Features:
- Warns if any line exceeds 80 characters
- Detects trailing spaces
- Checks for missing newline at end of file
- Lightweight, single-file script
"""

import sys
import os

def check_file(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"\n🔍 Analyzing '{file_path}'...\n")
    warnings = 0

    for i, line in enumerate(lines, start=1):
        if len(line.rstrip("\n")) > 80:
            print(f"⚠️  Line {i}: exceeds 80 characters ({len(line.rstrip())} chars)")
            warnings += 1

        if line.endswith(" \n"):
            print(f"⚠️  Line {i}: trailing whitespace detected")
            warnings += 1

        if "\t" in line:
            print(f"⚠️  Line {i}: tab character found (use 4 spaces instead)")
            warnings += 1

    # Check if file ends with a newline
    if not lines[-1].endswith("\n"):
        print("⚠️  File does not end with a newline")
        warnings += 1

    if warnings == 0:
        print("✅ No issues found. Code looks clean!")
    else:
        print(f"\n🧾 Total warnings: {warnings}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python pylintlite.py <filename.py>")
        return

    check_file(sys.argv[1])

if __name__ == "__main__":
    main()
