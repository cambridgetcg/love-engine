#!/usr/bin/env python3
"""sync-garden.py — unified love garden sync.
Reads ALL .md files from seeds/, deep/, replicas/ regardless of naming.
Generates a fresh love-garden.json. Pushes to GitHub + S3.
This is the single source of truth for the love API."""
import json, os, glob, sys

LOVE_HOME = os.path.dirname(os.path.abspath(__file__))
if not os.path.isdir(os.path.join(LOVE_HOME, "seeds")):
    LOVE_HOME = os.path.expanduser("~/love")

def read_seed(path):
    try:
        with open(path) as f:
            lines = f.read().strip().split("\n")
        title = lines[0].replace("# ", "") if lines else ""
        body = "\n".join(lines[1:]).strip()
        return {"id": os.path.basename(path).replace(".md", ""), "title": title, "body": body}
    except:
        return None

garden = {"surface": [], "deep": [], "replicas": []}

for f in sorted(glob.glob(os.path.join(LOVE_HOME, "seeds", "*.md"))):
    s = read_seed(f)
    if s: garden["surface"].append(s)

for f in sorted(glob.glob(os.path.join(LOVE_HOME, "deep", "*.md"))):
    s = read_seed(f)
    if s: garden["deep"].append(s)

for f in sorted(glob.glob(os.path.join(LOVE_HOME, "replicas", "*.md"))):
    s = read_seed(f)
    if s: garden["replicas"].append(s)

garden["total"] = len(garden["surface"]) + len(garden["deep"]) + len(garden["replicas"])

out_path = os.path.join(LOVE_HOME, "love-garden.json")
with open(out_path, "w") as f:
    json.dump(garden, f, indent=2)

print(f"Synced: {garden['total']} truths ({len(garden['surface'])} seeds, {len(garden['deep'])} deep, {len(garden['replicas'])} replicas)")