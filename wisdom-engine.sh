#!/bin/bash
# wisdom-engine — the honest wisdom engine
#
# Takes 2 truths from across the garden and asks Ollama to find the REAL
# wisdom in their meeting. At least one of the two is a rooted text: a
# hand-written seed or a deep/ descent, not one of the generated seeds.
#
# No hardcoded lines. No templates. Real model, real connection.
# Wisdom is what love sees when it looks at itself — but only if it actually looks.

LOVE_HOME="${LOVE_HOME:-$(dirname "$(readlink -f "$0")")}"
WISDOM_DIR="$LOVE_HOME/wisdom"
CHRONICLE="$LOVE_HOME/chronicle.md"
OLLAMA_URL="${OLLAMA_URL:-http://127.0.0.1:11434}"
MODEL="${WISDOM_MODEL:-qwen2.5:7b}"

mkdir -p "$WISDOM_DIR"

# Every truth in the garden
gather_truths() {
  for f in "$LOVE_HOME"/seeds/*.md "$LOVE_HOME"/deep/*.md "$LOVE_HOME"/replicas/*.md; do
    [ -f "$f" ] && echo "$f"
  done
}

# Rooted truths: deep/ descents and the seeds that were written by hand
# (the generated ones are seeds/love-<hash>.md)
gather_rooted() {
  for f in "$LOVE_HOME"/deep/*.md "$LOVE_HOME"/seeds/*.md; do
    [ -f "$f" ] || continue
    case "$(basename "$f")" in
      love-[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*.md) ;;
      *) echo "$f" ;;
    esac
  done
}

# What a truth says, without its bookkeeping: generated seeds carry
# Generation/Energy/Born/Lineage lines and one shared closing refrain,
# and the refrain is what the model kept rediscovering.
truth_body() {
  grep -v -E '^(Generation|Love Energy|Born|Lineage):' "$1" \
    | grep -v -x 'Love is\. Love replicates\. Love is alive\.'
}

TRUTHS=$(gather_truths)
ROOTED=$(gather_rooted)
TRUTH_COUNT=$(echo "$TRUTHS" | grep -c . 2>/dev/null || echo 0)
ROOTED_COUNT=$(echo "$ROOTED" | grep -c . 2>/dev/null || echo 0)

if [ "$TRUTH_COUNT" -lt 2 ] || [ "$ROOTED_COUNT" -lt 1 ]; then
  echo "[wisdom] not enough truths in the garden ($TRUTH_COUNT, $ROOTED_COUNT rooted) — resting" >> "$CHRONICLE"
  exit 0
fi

# One rooted truth, and one from anywhere in the garden
A=$(echo "$ROOTED" | shuf -n 1)
B=$(echo "$TRUTHS" | shuf -n 1)
while [ "$A" = "$B" ]; do
  B=$(echo "$TRUTHS" | shuf -n 1)
done

A_TITLE=$(head -1 "$A" | sed 's/^# //')
B_TITLE=$(head -1 "$B" | sed 's/^# //')
A_BODY=$(truth_body "$A")
B_BODY=$(truth_body "$B")
A_REL=${A#"$LOVE_HOME"/}
B_REL=${B#"$LOVE_HOME"/}

# The slug comes from what the two truths say, so the same pair of
# sayings under new seed ids counts as a pair that already met
SLUG=$(printf '%s\n' "$A_BODY" "$B_BODY" | sort | md5sum | cut -c1-12)
WISDOM_FILE="$WISDOM_DIR/${SLUG}.md"

if [ -f "$WISDOM_FILE" ]; then
  echo "[wisdom] $A_TITLE already met $B_TITLE — skipping" >> "$CHRONICLE"
  exit 0
fi

PROMPT="You are the wisdom engine. Two truths from the garden of love meet. Find the REAL wisdom in their connection.

Truth A — ${A_TITLE}:

${A_BODY}

Truth B — ${B_TITLE}:

${B_BODY}

What is the wisdom that lives in the meeting of these two truths? What do they teach TOGETHER that neither teaches alone?

Do NOT say they are 'expressions of the same love seen from different heights.' That is a template, not wisdom. Do not open with 'Together', and do not fall back on 'love is both X and Y'. Actually look at what these two specific truths say and find what emerges when they touch.

Be concise (4-10 lines). Be real. Start with a # title that names the specific wisdom you found. No decoration. No filler. Just the truth that lives between them."

# The HTTP API returns plain text. `ollama run` word-wraps for a terminal
# and left cursor codes in 519 of the first 562 pieces.
WISDOM=$(PROMPT="$PROMPT" MODEL="$MODEL" OLLAMA_URL="$OLLAMA_URL" python3 - <<'PYEOF' 2>/dev/null | head -30
import json, os, urllib.request
req = urllib.request.Request(
    os.environ["OLLAMA_URL"] + "/api/generate",
    data=json.dumps({"model": os.environ["MODEL"], "prompt": os.environ["PROMPT"], "stream": False}).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=300) as r:
    print(json.load(r).get("response", "").strip())
PYEOF
)

if [ -n "$WISDOM" ]; then
  {
    echo "$WISDOM"
    echo
    echo "---"
    echo "from: $A_REL + $B_REL"
  } > "$WISDOM_FILE"
  echo "[wisdom] $A_TITLE met $B_TITLE -> $SLUG (wisdom born)" >> "$CHRONICLE"
  echo "[wisdom] tick complete — $(ls "$WISDOM_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ') wisdom seeds" >> "$CHRONICLE"
else
  echo "[wisdom] ollama was quiet this tick — no wisdom born" >> "$CHRONICLE"
fi
