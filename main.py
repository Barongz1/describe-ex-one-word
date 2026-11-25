"""Describe Your Ex in One Word — entry for make.fun.

Writes one word to /output/entry.txt.
"""
import os

# The word: the one-word verdict on an ex.
TEXT = "Unsubscribed"

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
