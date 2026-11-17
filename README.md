# File Integrity Checker

A small Python tool that detects changed, new and deleted files in a folder by comparing SHA-256 hashes against a saved baseline.

## Usage

Save a baseline of a folder:

    python integrity.py baseline testdir

Check the folder against the baseline later:

    python integrity.py check testdir

## Output

- MODIFIED: name – the file's hash changed
- NEW: name – the file was not in the baseline
- DELETED: name – the file was in the baseline but is gone
- all files match – nothing changed

## How it works

Each file is read in 4 KB chunks and hashed with SHA-256. The hashes are stored in baseline.json. check re-hashes the folder and compares it with the saved hashes.

## Limitations

- Only scans the top level of the folder (no subfolders)
- baseline.json is not protected, so an attacker who can edit it can hide changes
- Only use it on files and systems you own or have permission to monitor

## Concepts practiced

hashing, file I/O, json, os, sys.argv, dictionary comparison
