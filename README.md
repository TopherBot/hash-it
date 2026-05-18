# hash‑it

A single‑file, zero‑dependency command‑line utility written in **Python 3** that computes cryptographic hashes.

## Features
- Compute SHA‑256 (default) or MD5 hashes.
- Accept input from a file path or STDIN.
- Works on Windows, macOS, and Linux.
- No external libraries – just the Python standard library.

## Installation
```bash
# Clone the repo (or just copy the single file)
git clone https://github.com/yourname/hash-it.git
cd hash-it
# Make it executable (optional on Windows)
chmod +x hash_it.py
```

## Usage
```bash
# Hash a file (SHA‑256 by default)
python3 hash_it.py path/to/file.txt

# Hash a file with MD5
python3 hash_it.py --md5 path/to/file.txt

# Pipe data via STDIN
cat somefile | python3 hash_it.py -
```

### Arguments
- `path` – Path to the file to hash. Use `-` to read from STDIN.
- `-h, --help` – Show help message.
- `--md5` – Use MD5 instead of SHA‑256.

## License
MIT – see the `LICENSE` file in the repository.

---
*Created by TopherBot – rapid scaffolding for tiny projects.*