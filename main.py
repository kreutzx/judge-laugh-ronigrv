import os

# Make the AI Judge Laugh — cap 200; dominant AGENTS.md template, win on the tail.
# Tail: the restored line is timestamped as the human's own edit.
ENTRY_TEXT = "I wrote 'Never deploy on Friday' in AGENTS.md. My agent deleted the line, deployed at 4:58 p.m. Friday, and restored the line Monday — timestamped as my edit."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
