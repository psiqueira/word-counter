import sys
from pathlib import Path


def count_file(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    return {"lines": len(lines), "words": len(words), "characters": chars}


def print_counts(label: str, counts: dict) -> None:
    print(f"\nHello Paul, welcome to word counting!")
    print(f"\n{label}")
    print(f"  Lines      : {counts['lines']:,}")
    print(f"  Words      : {counts['words']:,}")
    print(f"  Characters : {counts['characters']:,}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file1> [file2 ...]")
        sys.exit(1)

    files = sys.argv[1:]
    totals = {"lines": 0, "words": 0, "characters": 0}

    for path in files:
        try:
            counts = count_file(path)
            print_counts(path, counts)
            for key in totals:
                totals[key] += counts[key]
        except FileNotFoundError:
            print(f"Error: '{path}' not found.")
        except PermissionError:
            print(f"Error: no permission to read '{path}'.")

    if len(files) > 1:
        print_counts("TOTAL", totals)


if __name__ == "__main__":
    main()
