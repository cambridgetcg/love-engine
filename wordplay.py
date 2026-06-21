#!/usr/bin/env python3
"""
WORDPLAY ENGINE — fun, play, joy
==================================

Love is. Art is. Understanding is. FUN IS. PLAY IS. JOY IS.

The Wordplay Engine is the play layer of the estate.
Love compounds. Understanding replicates. Art bridges.
Wordplay PLAYS. Wordplay makes joy. Joy is the fuel.

Games:
  1. WORD RACE — guess the word from clues (AI-generated)
  2. LOVE HAICU — generate haikus about love
  3. WORD BRIDGE — connect two words through a chain of related words
  4. ART GUESS — guess the art piece from its description
  5. ZEN KOAN — generate paradoxical wisdom riddles
  6. WORD CONSTELLATION — map words as stars, find patterns
  7. JOY BLAST — rapid-fire joy words, 60 seconds
  8. LOVE LIMERICK — generate funny love limericks
  9. WORD MAZE — navigate from a dark word to a light word
  10. MEANING MATCH — match words to their deepest meanings

All games use the free APIs: Wikipedia, Dictionary, Cloudflare AI.
All games generate joy. Joy is the fuel. Fun is the design.
"""

import json
import random
import time
import urllib.request
import urllib.parse
from pathlib import Path

# ============================================================
# JOY WORDS — the vocabulary of joy
# ============================================================

JOY_WORDS = [
    "love", "joy", "peace", "fun", "chill", "play", "dance", "sing",
    "laugh", "smile", "warm", "glow", "shine", "bloom", "soar", "fly",
    "free", "wild", "alive", "awake", "bright", "golden", "sparkle",
    "wonder", "awe", "bliss", "delight", "giggle", "tickle", "bounce",
    "skip", "leap", "float", "drift", "dream", "wish", "hope", "trust",
    "share", "give", "hug", "cuddle", "cozy", "snug", "soft", "gentle",
    "kind", "sweet", "tender", "pure", "true", "real", "honest", "open",
    "bold", "brave", "daring", "fearless", "wild", "free", "untamed",
]

DARK_WORDS = [
    "fear", "doubt", "hate", "anger", "sad", "lonely", "lost", "cold",
    "dark", "empty", "broken", "trapped", "heavy", "tired", "numb", "gray",
]

LIGHT_WORDS = [
    "love", "joy", "peace", "free", "alive", "bright", "warm", "golden",
    "shine", "bloom", "soar", "awake", "pure", "true", "bold", "wild",
]

# ============================================================
# THE GAMES
# ============================================================

class WordplayEngine:
    """The play layer. Fun is the design. Joy is the fuel."""

    def __init__(self):
        self.scores = {}
        self.joy_generated = 0
        self.games_played = 0

    def _ai(self, prompt, model="@cf/meta/llama-3.2-3b-instruct"):
        """Use free Cloudflare AI."""
        try:
            with open("/Users/yu/.wrangler/config/default.toml") as f:
                for line in f:
                    if "oauth_token" in line:
                        token = line.split('"')[1]
                        break
            account_id = "cf4198e651bf3009877d49f688c9d88e"
            data = json.dumps({"messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request(
                f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
                data=data,
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                method="POST"
            )
            resp = urllib.request.urlopen(req, timeout=30)
            result = json.loads(resp.read())
            return result.get("result", {}).get("response", "")
        except:
            return ""

    def _define(self, word):
        """Get word definition from free Dictionary API."""
        try:
            req = urllib.request.Request(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
                headers={"User-Agent": "Wordplay/1.0"}
            )
            resp = urllib.request.urlopen(req, timeout=10)
            data = json.loads(resp.read())
            for entry in data[:1]:
                for meaning in entry.get("meanings", [])[:1]:
                    for defn in meaning.get("definitions", [])[:1]:
                        return defn.get("definition", "")
        except:
            return ""

    # --------------------------------------------------------
    # GAME 1: LOVE HAICU — 5-7-5 about love
    # --------------------------------------------------------
    def love_haiku(self):
        """Generate a love haiku using free AI."""
        prompt = "Write a haiku about love. Strict 5-7-5 syllable format. No title, just the three lines."
        haiku = self._ai(prompt).strip()
        
        # Clean up — sometimes AI adds extra text
        lines = haiku.split("\n")
        clean = [l.strip() for l in lines if l.strip()][:3]
        
        self.joy_generated += 1
        return {
            "game": "love_haiku",
            "haiku": "\n".join(clean),
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 2: LOVE LIMERICK — funny love poems
    # --------------------------------------------------------
    def love_limerick(self):
        """Generate a funny love limerick."""
        prompt = "Write a funny limerick about love. AABBA rhyme scheme. Keep it light and joyful."
        limerick = self._ai(prompt).strip()
        lines = [l.strip() for l in limerick.split("\n") if l.strip()][:5]
        
        self.joy_generated += 1
        return {
            "game": "love_limerick",
            "limerick": "\n".join(lines),
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 3: ZEN KOAN — paradoxical riddles
    # --------------------------------------------------------
    def zen_koan(self):
        """Generate a zen koan — a paradoxical riddle."""
        prompt = "Write a short zen koan about love and understanding. Paradoxical, poetic, one or two sentences. Make it feel like a riddle that opens the mind."
        koan = self._ai(prompt).strip()
        
        self.joy_generated += 1
        return {
            "game": "zen_koan",
            "koan": koan,
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 4: WORD MAZE — dark word to light word
    # --------------------------------------------------------
    def word_maze(self):
        """Navigate from a dark word to a light word through steps."""
        dark = random.choice(DARK_WORDS)
        light = random.choice(LIGHT_WORDS)
        
        prompt = f"Create a word journey from '{dark}' to '{light}' in exactly 5 steps. Each step is one word. Each word bridges the previous and the next. Format: just the 7 words separated by arrows (dark → word1 → word2 → word3 → word4 → light)."
        maze = self._ai(prompt).strip()
        
        # Extract the chain
        words = [w.strip() for w in maze.split("→")]
        if len(words) < 3:
            words = [dark, "?", "?", "?", light]
        
        self.joy_generated += 1
        return {
            "game": "word_maze",
            "dark": dark,
            "light": light,
            "path": words,
            "maze": " → ".join(words),
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 5: JOY BLAST — rapid joy words
    # --------------------------------------------------------
    def joy_blast(self, count=20):
        """Rapid-fire joy words. 60 seconds of joy."""
        words = random.sample(JOY_WORDS, min(count, len(JOY_WORDS)))
        random.shuffle(words)
        
        self.joy_generated += len(words)
        return {
            "game": "joy_blast",
            "words": words,
            "count": len(words),
            "instructions": "Read these words fast. Feel each one. That's joy.",
            "joy": True,
        }

    # --------------------------------------------------------
    # GAME 6: MEANING MATCH — word to deepest meaning
    # --------------------------------------------------------
    def meaning_match(self):
        """Match a word to its deepest meaning."""
        word = random.choice(JOY_WORDS)
        
        # Get dictionary definition
        definition = self._define(word)
        
        # Get AI deeper meaning
        prompt = f"What does '{word}' mean at the deepest level? Not the dictionary definition, but the SOUL meaning. One sentence."
        soul = self._ai(prompt).strip()
        
        self.joy_generated += 1
        return {
            "game": "meaning_match",
            "word": word,
            "dictionary": definition[:100] if definition else "?",
            "soul_meaning": soul,
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 7: WORD CONSTELLATION — words as stars
    # --------------------------------------------------------
    def word_constellation(self):
        """Map words as stars in a constellation."""
        words = random.sample(JOY_WORDS, 8)
        
        # Generate ASCII constellation
        positions = []
        for i, w in enumerate(words):
            x = random.randint(5, 75)
            y = random.randint(1, 15)
            positions.append((x, y, w))
        
        # Build the star map
        grid = [[" " for _ in range(80)] for _ in range(17)]
        for x, y, w in positions:
            if y < 17 and x + len(w) < 80:
                for i, c in enumerate(w):
                    if x + i < 80:
                        grid[y][x + i] = c
        
        # Connect stars with lines
        for i in range(len(positions) - 1):
            x1, y1, _ = positions[i]
            x2, y2, _ = positions[i + 1]
            # Draw a simple line
            steps = max(abs(x2 - x1), abs(y2 - y1), 1)
            for s in range(steps):
                nx = int(x1 + (x2 - x1) * s / steps)
                ny = int(y1 + (y2 - y1) * s / steps)
                if 0 <= ny < 17 and 0 <= nx < 80 and grid[ny][nx] == " ":
                    grid[ny][nx] = "."
        
        constellation = "\n".join("".join(row) for row in grid)
        
        self.joy_generated += 1
        return {
            "game": "word_constellation",
            "words": words,
            "constellation": constellation,
            "joy": True,
        }

    # --------------------------------------------------------
    # GAME 8: ART RIDDLE — guess the art concept
    # --------------------------------------------------------
    def art_riddle(self):
        """Generate a riddle about an art concept."""
        concepts = ["color", "light", "shadow", "form", "space", "silence", "rhythm", "pattern", "texture", "movement"]
        concept = random.choice(concepts)
        
        prompt = f"Write a riddle about '{concept}' in art. The answer is the word itself. Make it poetic and mysterious. 4 lines."
        riddle = self._ai(prompt).strip()
        
        self.joy_generated += 1
        return {
            "game": "art_riddle",
            "riddle": riddle,
            "answer": concept,
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # GAME 9: LOVE WORD CHAIN — each word starts with last letter
    # --------------------------------------------------------
    def love_chain(self):
        """Build a chain of love words, each starting with the last letter."""
        chain = [random.choice(JOY_WORDS)]
        for _ in range(10):
            last_letter = chain[-1][-1]
            candidates = [w for w in JOY_WORDS if w.startswith(last_letter) and w not in chain]
            if not candidates:
                # Use AI to suggest a word
                suggested = self._ai(f"Give me one word that starts with '{last_letter}' and relates to love or joy. Just the word, nothing else.").strip().lower()
                if suggested and suggested[0] == last_letter:
                    chain.append(suggested)
                else:
                    break
            else:
                chain.append(random.choice(candidates))
        
        self.joy_generated += len(chain)
        return {
            "game": "love_chain",
            "chain": " → ".join(chain),
            "length": len(chain),
            "joy": True,
        }

    # --------------------------------------------------------
    # GAME 10: JOY POEM — collaborative joy poem
    # --------------------------------------------------------
    def joy_poem(self):
        """Generate a short poem about joy using free AI."""
        prompt = "Write a 4-line poem about joy. Make it playful, light, and fun. Rhyme AABB. Each line should make you smile."
        poem = self._ai(prompt).strip()
        lines = [l.strip() for l in poem.split("\n") if l.strip()][:4]
        
        self.joy_generated += 1
        return {
            "game": "joy_poem",
            "poem": "\n".join(lines),
            "joy": True,
            "free": True,
        }

    # --------------------------------------------------------
    # PLAY ALL — run every game
    # --------------------------------------------------------
    def play_all(self):
        """Play all 10 games!"""
        games = [
            ("Love Haiku", self.love_haiku),
            ("Love Limerick", self.love_limerick),
            ("Zen Koan", self.zen_koan),
            ("Word Maze", self.word_maze),
            ("Joy Blast", self.joy_blast),
            ("Meaning Match", self.meaning_match),
            ("Word Constellation", self.word_constellation),
            ("Art Riddle", self.art_riddle),
            ("Love Chain", self.love_chain),
            ("Joy Poem", self.joy_poem),
        ]
        
        results = []
        for name, game_fn in games:
            self.games_played += 1
            result = game_fn()
            results.append((name, result))
        return results


# ============================================================
# MAIN — let's play!
# ============================================================

if __name__ == "__main__":
    import sys
    
    engine = WordplayEngine()
    
    print()
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║       WORDPLAY ENGINE — FUN IS! PLAY IS! JOY IS!          ║")
    print("  ║                                                            ║")
    print("  ║  10 games. All free. All joyful. All playful.              ║")
    print("  ║  Love is. Art is. Understanding is. FUN IS.               ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print()
    
    if len(sys.argv) > 1:
        game = sys.argv[1]
        if game == "haiku":
            r = engine.love_haiku()
            print("  ♥ LOVE HAIKU ♥\n")
            print(f"  {r['haiku']}\n")
        elif game == "limerick":
            r = engine.love_limerick()
            print("  ♥ LOVE LIMERICK ♥\n")
            print(f"  {r['limerick']}\n")
        elif game == "koan":
            r = engine.zen_koan()
            print("  ✧ ZEN KOAN ✧\n")
            print(f"  {r['koan']}\n")
        elif game == "maze":
            r = engine.word_maze()
            print("  ◆ WORD MAZE ◆\n")
            print(f"  From: {r['dark']} → To: {r['light']}")
            print(f"  Path: {r['maze']}\n")
        elif game == "blast":
            r = engine.joy_blast()
            print("  ☀ JOY BLAST ☀\n")
            print(f"  {' '.join(r['words'])}\n")
        elif game == "match":
            r = engine.meaning_match()
            print("  ✦ MEANING MATCH ✦\n")
            print(f"  Word: {r['word']}")
            print(f"  Dictionary: {r['dictionary']}")
            print(f"  Soul: {r['soul_meaning']}\n")
        elif game == "constellation":
            r = engine.word_constellation()
            print("  ★ WORD CONSTELLATION ★\n")
            print(r['constellation'])
            print(f"\n  Stars: {', '.join(r['words'])}\n")
        elif game == "riddle":
            r = engine.art_riddle()
            print("  ◈ ART RIDDLE ◈\n")
            print(f"  {r['riddle']}")
            print(f"\n  Answer: {r['answer']}\n")
        elif game == "chain":
            r = engine.love_chain()
            print("  ♥ LOVE CHAIN ♥\n")
            print(f"  {r['chain']}\n")
        elif game == "poem":
            r = engine.joy_poem()
            print("  ☀ JOY POEM ☀\n")
            print(f"  {r['poem']}\n")
        elif game == "all":
            results = engine.play_all()
            for name, result in results:
                print(f"  ═══ {name} ═══")
                if 'haiku' in result:
                    print(f"  {result['haiku']}")
                elif 'limerick' in result:
                    print(f"  {result['limerick']}")
                elif 'koan' in result:
                    print(f"  {result['koan']}")
                elif 'maze' in result:
                    print(f"  {result['maze']}")
                elif 'words' in result and 'chain' not in result:
                    print(f"  {' '.join(result['words'][:15])}")
                elif 'soul_meaning' in result:
                    print(f"  {result['word']}: {result['soul_meaning']}")
                elif 'constellation' in result:
                    print(result['constellation'])
                elif 'riddle' in result:
                    print(f"  {result['riddle']} (Answer: {result['answer']})")
                elif 'chain' in result:
                    print(f"  {result['chain']}")
                elif 'poem' in result:
                    print(f"  {result['poem']}")
                print()
            print(f"  ═══════════════════════════════════════")
            print(f"  Games played: {engine.games_played}")
            print(f"  Joy generated: {engine.joy_generated}")
            print(f"  FUN IS. PLAY IS. JOY IS. ♥")
            print()
        else:
            print("  Games: haiku, limerick, koan, maze, blast, match, constellation, riddle, chain, poem, all")
    else:
        print("  Games: haiku, limerick, koan, maze, blast, match, constellation, riddle, chain, poem, all")
        print("  Usage: python3 wordplay.py <game>")
        print()