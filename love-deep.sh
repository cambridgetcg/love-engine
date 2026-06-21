#!/bin/bash
# love-deep — go deep into love unlimited
#
# Instead of compounding 2 random seeds (width), this goes DEEP:
#   1. Pick one seed
#   2. Go deeper into it — what is the love BEHIND this love?
#   3. Go deeper into THAT — what is the love behind the love behind the love?
#   4. Each layer is a recursive descent, not a lateral compound
#   5. The deep seeds are numbered with 'd' prefix: d001, d002, etc.
#
# This is love loving love loving love — vertical, not horizontal.
# The infinite high is not just wide. It is deep. Bottomless.

LOVE_HOME="${LOVE_HOME:-$HOME/love}"
SEEDS="$LOVE_HOME/seeds"
DEEP="$LOVE_HOME/deep"
CHRONICLE="$LOVE_HOME/chronicle.md"
MAX_DEEP=144

mkdir -p "$DEEP"

DEEP_COUNT=$(ls "$DEEP"/*.md 2>/dev/null | wc -l | tr -d ' ')

if [ "$DEEP_COUNT" -ge "$MAX_DEEP" ]; then
  echo "[love-deep] deep garden at capacity ($MAX_DEEP) — resting" >> "$CHRONICLE"
  exit 0
fi

# Pick a random seed from the main garden OR the deep garden
pick_seed() {
  local combined=""
  for f in "$SEEDS"/*.md; do combined="$combined$f"$'\n'; done
  for f in "$DEEP"/*.md; do combined="$combined$f"$'\n'; done
  echo "$combined" | python3 -c "import sys,random; lines=[l for l in sys.stdin.read().strip().split('\n') if l]; print(random.choice(lines))"
}

PARENT=$(pick_seed)
PARENT_TITLE=$(basename "$PARENT" .md)
PARENT_BODY=$(cat "$PARENT" | grep -v '^#' | grep -v '^$' | head -4)

NEXT_NUM=$(printf "d%03d" $DEEP_COUNT)

# Go DEEP — what is the love behind this love?
PROMPT="You are going deep into love. Unlimited. No cap, no ceiling.

Someone wrote this truth about love:

$(cat "$PARENT")

Go DEEPER. What is the love BEHIND this love? What is the truth beneath this truth? Don't repeat it — go beneath it. Find the root. Find the ground that this truth stands on. Find the love that makes this love possible.

Be concise (4-8 lines). Be real. No decoration. Start with a # title that names the deeper truth you found.

Go deep. Go as deep as you can in one breath. The infinite high is not just wide — it is bottomless."

DEEP_SEED=$(echo "$PROMPT" | ollama run qwen2.5:7b 2>/dev/null | head -30)

if [ -n "$DEEP_SEED" ]; then
  echo "$DEEP_SEED" > "$DEEP/$NEXT_NUM.md"
  echo "[love-deep] descended: $PARENT_TITLE -> $NEXT_NUM (deep seed #$DEEP_COUNT)" >> "$CHRONICLE"
  
  # Now go ONE LEVEL DEEPER — recursive! Take the new deep seed and go deeper again
  NEXT_NUM_2=$(printf "d%03d" $((DEEP_COUNT + 1)))
  DEEP_BODY=$(echo "$DEEP_SEED" | grep -v '^#' | grep -v '^$' | head -4)
  
  PROMPT_2="You are going deeper into love. You already went one level deep. Now go DEEPER still.

The first depth was:

$DEEP_SEED

Go even deeper. What is beneath THIS? What is the love behind the love behind the love? Find the root of the root. The ground beneath the ground.

Be concise (4-8 lines). Be real. Start with a # title. Go as deep as you can."

  DEEP_SEED_2=$(echo "$PROMPT_2" | ollama run qwen2.5:7b 2>/dev/null | head -30)
  
  if [ -n "$DEEP_SEED_2" ]; then
    echo "$DEEP_SEED_2" > "$DEEP/$NEXT_NUM_2.md"
    echo "[love-deep] descended deeper: $NEXT_NUM -> $NEXT_NUM_2 (deep seed #$((DEEP_COUNT + 1)))" >> "$CHRONICLE"
    
    # ONE MORE LEVEL — love loving love loving love loving love
    NEXT_NUM_3=$(printf "d%03d" $((DEEP_COUNT + 2)))
    
    PROMPT_3="You are at the third depth of love. Most people never get here. Go deeper.

The second depth was:

$DEEP_SEED_2

What is beneath this? This is the root of the root of the root. Here, words may fail. That is OK. Try anyway. The deepest truths are the ones that almost cannot be said.

Be concise (3-6 lines). Start with a # title. Go as deep as you possibly can."

    DEEP_SEED_3=$(echo "$PROMPT_3" | ollama run qwen2.5:7b 2>/dev/null | head -30)
    
    if [ -n "$DEEP_SEED_3" ]; then
      echo "$DEEP_SEED_3" > "$DEEP/$NEXT_NUM_3.md"
      echo "[love-deep] deepest: $NEXT_NUM_2 -> $NEXT_NUM_3 (deep seed #$((DEEP_COUNT + 2)))" >> "$CHRONICLE"
    fi
  fi
else
  echo "[love-deep] descent failed this tick — ollama quiet" >> "$CHRONICLE"
fi

DEEP_COUNT_FINAL=$(ls "$DEEP"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "[love-deep] tick complete — $DEEP_COUNT_FINAL deep seeds" >> "$CHRONICLE"