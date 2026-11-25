#!/usr/bin/env python3
"""Writes the make.fun nostalgic childhood-memory entry to /output/entry.txt."""

import os

ENTRY = (
    "Every evening after school I sat on Grandma's cold kitchen tiles in my socks, "
    "breathing in fresh rice and woodsmoke, waiting for her to ladle the first "
    "scoop into my bowl and tell me to blow on it before it burned my tongue."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
