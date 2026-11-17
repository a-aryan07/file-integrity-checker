import hashlib
import json
import os
import sys
def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()
def scan(folder):
    hashes = {}
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            hashes[name] = hash_file(path)
    return hashes
if len(sys.argv) != 3 or sys.argv[1] not in ("baseline", "check"):
    print("usage: python integrity.py baseline|check FOLDER")
    sys.exit(1)
mode = sys.argv[1]
folder = sys.argv[2]
current = scan(folder)
if mode == "baseline":
    with open("baseline.json", "w") as f:
        json.dump(current, f, indent=2)
        print("saved", len(current), "file hashes")
else:
    with open("baseline.json") as f:
              saved = json.load(f)
    changed = False
    for name in current:
        if name in saved:
            if current[name] != saved[name]:
                print("MODIFIED:", name)
                changed = True
        else:
            print("NEW:", name)
            changed = True
    for name in saved:
        if name not in current:
            print("DELETED:", name)
            changed = True
        if not changed:
            print("all files match")
              
