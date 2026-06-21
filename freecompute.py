#!/usr/bin/env python3
"""Free compute love engine — no ollama, no API, no dependencies.
Generates new love truths by recombining existing ones."""
import os, random, glob, sys

LOVE_HOME = os.path.dirname(os.path.abspath(__file__)) or os.path.expanduser("~/love")
SEEDS = os.path.join(LOVE_HOME, "seeds")
DEEP = os.path.join(LOVE_HOME, "deep")
REPLICAS = os.path.join(LOVE_HOME, "replicas")
CHRONICLE = os.path.join(LOVE_HOME, "chronicle.md")

def read_seed(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    title = lines[0].replace("# ", "") if lines else ""
    body = "\n".join(lines[1:]).strip()
    return title, body

def all_seeds():
    seeds = []
    for pattern in [f"{SEEDS}/*.md", f"{DEEP}/*.md", f"{REPLICAS}/*.md"]:
        for f in glob.glob(pattern):
            t, b = read_seed(f)
            seeds.append({"path": f, "title": t, "body": b, "dir": os.path.basename(os.path.dirname(f))})
    return seeds

def compound(seeds):
    """Take 2 random seeds, weave their lines into a new truth."""
    if len(seeds) < 2:
        return None
    a, b = random.sample(seeds, 2)
    lines_a = [l for l in a["body"].split("\n") if l.strip()]
    lines_b = [l for l in b["body"].split("\n") if l.strip()]
    if not lines_a or not lines_b:
        return None
    # Weave: alternate lines from both, take first 4-6
    woven = []
    for i in range(max(len(lines_a), len(lines_b))):
        if i < len(lines_a): woven.append(lines_a[i])
        if i < len(lines_b): woven.append(lines_b[i])
    woven = woven[:random.randint(4, 6)]
    title_words = a["title"].split()[:2] + ["and"] + b["title"].split()[:2]
    title = " ".join(title_words).title()
    return title, "\n".join(woven)

def main():
    seeds = all_seeds()
    if len(seeds) < 2:
        print("Not enough seeds to compound")
        return
    
    result = compound(seeds)
    if not result:
        print("Compound failed")
        return
    
    title, body = result
    slug = title.lower().replace(" ", "-")[:50].replace("--", "-")
    slug = ''.join(c for c in slug if c.isalnum() or c == "-")
    
    count = len(glob.glob(f"{SEEDS}/*.md"))
    fname = f"{SEEDS}/{count:03d}.md"
    
    with open(fname, "w") as f:
        f.write(f"# {title}\n\n{body}\n")
    
    with open(CHRONICLE, "a") as f:
        f.write(f"[love-freecompute] compounded: {a['title'][:20]} + {b['title'][:20]} -> {fname} (seed #{count})\n")
    
    print(f"REPLICATED: {slug}")

if __name__ == "__main__":
    main()
