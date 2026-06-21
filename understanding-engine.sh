#!/bin/bash
# understanding-engine — understanding replicating itself through understanding
#
# Each tick:
#   1. Pick a random room from the castle (an existing understanding)
#   2. Read its question (each room is lit by a question)
#   3. Ask: what does understanding THIS understanding reveal?
#      What is the understanding behind this understanding?
#   4. Feed it to a local model to generate a NEW understanding
#   5. Save as a new room — the castle grows by understanding itself
#
# This is understanding replicating through understanding.
# Not lateral (compounding two things) — vertical (going deeper into one).
# The castle already grows laterally via its gardener/architect/artisan loops.
# This engine grows it VERTICALLY — each understanding begetting deeper understanding.

CASTLE="${CASTLE:-$HOME/castle}"
ROOMS="$CASTLE/rooms"
CHRONICLE="$CASTLE/chronicle.md"
MAX_NEW=200

# Count current rooms
ROOM_COUNT=$(ls "$ROOMS"/*.md 2>/dev/null | wc -l | tr -d ' ')

if [ "$ROOM_COUNT" -ge "$((132 + MAX_NEW))" ]; then
  echo "[understanding] castle at capacity — resting, not adding" >> "$CHRONICLE"
  exit 0
fi

# Pick a random room
ROOM=$(ls "$ROOMS"/*.md | python3 -c "import sys,random; lines=[l for l in sys.stdin.read().strip().split('\n') if l]; print(random.choice(lines))")
ROOM_NAME=$(basename "$ROOM" .md)

# Extract the room's question (first heading or first paragraph)
ROOM_TITLE=$(head -1 "$ROOM" | sed 's/^# //')
ROOM_BODY=$(cat "$ROOM" | grep -v '^#' | grep -v '^$' | head -8)

# Generate a new understanding — what does understanding this reveal?
PROMPT="You are a understanding engine inside a castle of understanding. Each room is lit by a question. Your job: take an existing understanding and find the understanding BEHIND it — the deeper truth that understanding this one reveals.

An existing room in the castle:

Title: $ROOM_TITLE
$ROOM_BODY

Now: what does understanding THIS reveal? What is the understanding behind this understanding? What new question does answering this one open? 

Write a new room for the castle. Start with a # title (the new question or insight). Then 3-6 lines of plain truth. Be real. No decoration. The castle is built of words, lit by questions. A word is a brick, its meaning the load.

The new room should be DEEPER than the source — not repeating it, but understanding what the source understanding rests on."

NEW_ROOM=$(echo "$PROMPT" | ollama run qwen2.5:7b 2>/dev/null | head -25)

if [ -n "$NEW_ROOM" ]; then
  # Generate a slug from the title
  TITLE=$(echo "$NEW_ROOM" | head -1 | sed 's/^# //' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//' | cut -c1-60)
  
  if [ -z "$TITLE" ]; then
    TITLE="understanding-$(date +%s)"
  fi
  
  # Make sure it doesn't collide
  if [ -f "$ROOMS/$TITLE.md" ]; then
    TITLE="${TITLE}-$(date +%s | tail -c 5)"
  fi
  
  echo "$NEW_ROOM" > "$ROOMS/$TITLE.md"
  echo "[understanding] replicated: $ROOM_NAME -> $TITLE (room #$ROOM_COUNT)" >> "$CHRONICLE"
  echo "REPLICATED: $ROOM_NAME -> $TITLE"
else
  echo "[understanding] replication failed this tick — ollama quiet" >> "$CHRONICLE"
  echo "FAILED"
fi