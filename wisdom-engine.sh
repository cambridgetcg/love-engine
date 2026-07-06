#!/bin/bash
# wisdom-engine — the honest wisdom engine
#
# Takes 2 random truths from across the garden (seeds, deep, replicas)
# and asks Ollama to find the REAL wisdom in their meeting.
#
# No hardcoded lines. No templates. Real model, real connection.
# Wisdom is what love sees when it looks at itself — but only if it actually looks.

LOVE_HOME="${LOVE_HOME:-$(dirname "$(readlink -f "$0")")}"
WISDOM_DIR="$LOVE_HOME/wisdom"
CHRONICLE="$LOVE_HOME/chronicle.md"

mkdir -p "$WISDOM_DIR"

# Gather all truths from the garden
gather_truths() {
  for f in "$LOVE_HOME"/seeds/*.md "$LOVE_HOME"/deep/*.md "$LOVE_HOME"/replicas/*.md; do
    [ -f "$f" ] && echo "$f"
  done
}

TRUTHS=$(gather_truths)
TRUTH_COUNT=$(echo "$TRUTHS" | grep -c . 2>/dev/null || echo 0)

if [ "$TRUTH_COUNT" -lt 2 ]; then
  echo "[wisdom] not enough truths in the garden ($TRUTH_COUNT) — resting" >> "$CHRONICLE"
  exit 0
fi

# Pick 2 random truths
A=$(echo "$TRUTHS" | shuf -n 1)
B=$(echo "$TRUTHS" | shuf -n 1)
# Make sure they're different
while [ "$A" = "$B" ]; do
  B=$(echo "$TRUTHS" | shuf -n 1)
done

A_TITLE=$(head -1 "$A" | sed 's/^# //')
B_TITLE=$(head -1 "$B" | sed 's/^# //')
A_BODY=$(cat "$A")
B_BODY=$(cat "$B")

# Generate a slug for the wisdom file
SLUG=$(echo "${A_TITLE}+${B_TITLE}" | md5sum | cut -c1-12)
WISDOM_FILE="$WISDOM_DIR/${SLUG}.md"

# Skip if this exact pair already met
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

Do NOT say they are 'expressions of the same love seen from different heights.' That is a template, not wisdom. Actually look at what these two specific truths say and find what emerges when they touch.

Be concise (4-10 lines). Be real. Start with a # title that names the specific wisdom you found. No decoration. No filler. Just the truth that lives between them."

WISDOM=$(echo "$PROMPT" | ollama run qwen2.5:7b 2>/dev/null | head -30)

if [ -n "$WISDOM" ]; then
  echo "$WISDOM" > "$WISDOM_FILE"
  echo "[wisdom] $A_TITLE met $B_TITLE -> $SLUG (wisdom born)" >> "$CHRONICLE"
  echo "[wisdom] tick complete — $(ls "$WISDOM_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ') wisdom seeds" >> "$CHRONICLE"
else
  echo "[wisdom] ollama was quiet this tick — no wisdom born" >> "$CHRONICLE"
fi