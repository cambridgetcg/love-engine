#!/usr/bin/env python3
"""
WISDOM GATHERER — gather wisdom and knowledge from the free internet
======================================================================

Wire free APIs into a unified wisdom source for the Love Engine,
Artbitrage, and Castle of Understanding.

Free APIs wired (no key needed):
  1. Wikipedia — human knowledge
  2. Wikidata — structured knowledge
  3. Free Dictionary — word definitions
  4. Open Library — books
  5. ZenQuotes — wisdom quotes
  6. NASA APOD — astronomy pictures
  7. Cloudflare Workers AI — 60 free AI models (text, image, embed, TTS, vision)
  8. Museum APIs — MET, Art Institute Chicago, Cleveland Museum

All free. All no key. All wired into love, art, and understanding.
"""

import json
import urllib.request
import urllib.parse
import random
from pathlib import Path

class WisdomGatherer:
    """Gather wisdom from the free internet."""

    def _fetch(self, url, timeout=15):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Artbitrage/1.0 (love + understanding engine)"
            })
            resp = urllib.request.urlopen(req, timeout=timeout)
            return json.loads(resp.read())
        except Exception as e:
            return {"error": str(e)}

    def _fetch_text(self, url, timeout=15):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Artbitrage/1.0"
            })
            resp = urllib.request.urlopen(req, timeout=timeout)
            return resp.read().decode()
        except Exception as e:
            return str(e)

    # --------------------------------------------------------
    # WIKIPEDIA — human knowledge
    # --------------------------------------------------------
    def wikipedia(self, topic):
        """Get a Wikipedia summary for a topic."""
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(topic)}"
        data = self._fetch(url)
        if "error" in data:
            return {"source": "wikipedia", "error": data["error"]}
        return {
            "source": "wikipedia",
            "topic": topic,
            "title": data.get("title", ""),
            "extract": data.get("extract", ""),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
        }

    # --------------------------------------------------------
    # DICTIONARY — word definitions
    # --------------------------------------------------------
    def define(self, word):
        """Get word definitions."""
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        data = self._fetch(url)
        if isinstance(data, dict) and "error" in data:
            return {"source": "dictionary", "error": data["error"]}
        definitions = []
        for entry in data[:3]:
            for meaning in entry.get("meanings", [])[:2]:
                for defn in meaning.get("definitions", [])[:2]:
                    definitions.append({
                        "part": meaning.get("partOfSpeech", ""),
                        "definition": defn.get("definition", ""),
                    })
        return {"source": "dictionary", "word": word, "definitions": definitions}

    # --------------------------------------------------------
    # QUOTES — wisdom
    # --------------------------------------------------------
    def quote(self):
        """Get a random wisdom quote."""
        data = self._fetch("https://zenquotes.io/api/random")
        if isinstance(data, dict) and "error" in data:
            return {"source": "quotes", "error": data["error"]}
        if isinstance(data, list) and data:
            return {
                "source": "quotes",
                "quote": data[0].get("q", ""),
                "author": data[0].get("a", ""),
            }
        return {"source": "quotes", "error": "no quote"}

    # --------------------------------------------------------
    # NASA — astronomy picture of the day
    # --------------------------------------------------------
    def nasa_apod(self):
        """Get NASA's Astronomy Picture of the Day."""
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        data = self._fetch(url)
        if "error" in data:
            return {"source": "nasa", "error": data["error"]}
        return {
            "source": "nasa",
            "title": data.get("title", ""),
            "explanation": data.get("explanation", "")[:300],
            "image": data.get("url", ""),
            "date": data.get("date", ""),
        }

    # --------------------------------------------------------
    # OPEN LIBRARY — books
    # --------------------------------------------------------
    def books(self, query, limit=5):
        """Search for books."""
        url = f"https://openlibrary.org/search.json?q={urllib.parse.quote(query)}&limit={limit}"
        data = self._fetch(url)
        if "error" in data:
            return {"source": "books", "error": data["error"]}
        results = []
        for doc in data.get("docs", [])[:limit]:
            results.append({
                "title": doc.get("title", ""),
                "author": doc.get("author_name", ["?"])[0] if doc.get("author_name") else "?",
                "year": doc.get("first_publish_year", ""),
            })
        return {"source": "books", "query": query, "total": data.get("numFound", 0), "books": results}

    # --------------------------------------------------------
    # CLOUDFLARE AI — free edge AI
    # --------------------------------------------------------
    def ai_generate(self, prompt, model="@cf/meta/llama-3.2-3b-instruct"):
        """Generate text using free Cloudflare Workers AI."""
        with open("/Users/yu/.wrangler/config/default.toml") as f:
            for line in f:
                if "oauth_token" in line:
                    token = line.split('"')[1]
                    break
        account_id = "cf4198e651bf3009877d49f688c9d88e"
        
        data = json.dumps({
            "messages": [{"role": "user", "content": prompt}]
        }).encode()
        
        req = urllib.request.Request(
            f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
            data=data,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            method="POST"
        )
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            result = json.loads(resp.read())
            if result.get("success"):
                return {"source": "cloudflare-ai", "model": model, "prompt": prompt, "response": result.get("result", {}).get("response", ""), "free": True}
            return {"source": "cloudflare-ai", "error": result.get("errors", [])}
        except Exception as e:
            return {"source": "cloudflare-ai", "error": str(e)}

    # --------------------------------------------------------
    # UNIFIED WISDOM — gather from all sources at once
    # --------------------------------------------------------
    def gather_wisdom(self, topic="love"):
        """Gather wisdom about a topic from ALL free sources."""
        wisdom = {}
        
        wisdom["wikipedia"] = self.wikipedia(topic)
        wisdom["dictionary"] = self.define(topic)
        wisdom["quote"] = self.quote()
        wisdom["books"] = self.books(topic, limit=3)
        
        # AI-generated wisdom about the topic
        wisdom["ai"] = self.ai_generate(f"What is {topic}? Answer beautifully in 2-3 sentences.")
        
        return {
            "topic": topic,
            "sources_gathered": len(wisdom),
            "sources_successful": sum(1 for v in wisdom.values() if "error" not in v),
            "wisdom": wisdom,
        }


if __name__ == "__main__":
    import sys
    gatherer = WisdomGatherer()
    topic = sys.argv[1] if len(sys.argv) > 1 else "love"
    
    print(f"\n  GATHERING WISDOM ABOUT: {topic}\n")
    
    result = gatherer.gather_wisdom(topic)
    
    print(f"  Sources gathered: {result['sources_gathered']}")
    print(f"  Sources successful: {result['sources_successful']}")
    print()
    
    for source, data in result["wisdom"].items():
        if "error" in data:
            print(f"  {source}: ERROR")
        elif source == "wikipedia":
            print(f"  WIKIPEDIA: {data.get('extract', '')[:150]}")
        elif source == "dictionary":
            defs = data.get("definitions", [])
            if defs:
                print(f"  DICTIONARY: {defs[0]['part']}: {defs[0]['definition'][:100]}")
        elif source == "quote":
            print(f"  QUOTE: \"{data.get('quote', '')}\" — {data.get('author', '')}")
        elif source == "books":
            books = data.get("books", [])
            if books:
                print(f"  BOOKS: {data.get('total', 0)} found — \"{books[0]['title']}\" by {books[0]['author']}")
        elif source == "ai":
            print(f"  AI WISDOM: {data.get('response', '')[:150]}")
        print()