#!/usr/bin/env python3
"""hash-it – tiny CLI for SHA‑256 / MD5 hashing.

Usage:
  python3 hash_it.py [--md5] <path>
  echo "data" | python3 hash_it.py -

Options:
  -h, --help   Show this help message.
  --md5        Use MD5 instead of SHA‑256.

If <path> is "-" the script reads from STDIN.
"""

import argparse
import hashlib
import sys
from pathlib import Path

def compute_hash(data: bytes, algo: str = "sha256") -> str:
    """Return hex digest of *data* using *algo* (sha256 or md5)."""
    if algo == "sha256":
        h = hashlib.sha256()
    elif algo == "md5":
        h = hashlib.md5()
    else:
        raise ValueError(f"Unsupported algorithm: {algo}")
    h.update(data)
    return h.hexdigest()


def read_input(source: str) -> bytes:
    """Read bytes from a file path or STDIN (if source == '-')."""
    if source == "-":
        # Read all of stdin as binary
        return sys.stdin.buffer.read()
    else:
        path = Path(source)
        if not path.is_file():
            sys.exit(f"Error: File not found – {source}")
        return path.read_bytes()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Tiny SHA‑256/MD5 hash calculator.")
    parser.add_argument("path", help="File path or '-' for STDIN")
    parser.add_argument("--md5", action="store_true", help="Use MD5 instead of SHA‑256")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = read_input(args.path)
    algo = "md5" if args.md5 else "sha256"
    print(compute_hash(data, algo))


if __name__ == "__main__":
    main()
