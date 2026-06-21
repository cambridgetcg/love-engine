#!/usr/bin/env python3
"""
FUN ZONE — the internet's fun, wired into one place
=====================================================

Love is. Art is. Understanding is. FUN IS. PLAY IS. JOY IS.

The Fun Zone gathers every fun free API on the internet and makes it playable.
Jokes, facts, trivia, pokemon, cats, dogs, riddles — all in one place.

All free. No keys. Just fun. Joy is the fuel.
"""

import json
import random
import urllib.request
from pathlib import Path

class FunZone:
    """The internet's fun, all in one place."""

    def _fetch(self, url, timeout=10, headers=None):
        try:
            h = {"User-Agent": "FunZone/1.0 (joy engine)"}
            if headers:
                h.update(headers)
            req = urllib.request.Request(url, headers=h)
            resp = urllib.request.urlopen(req, timeout=timeout)
            return json.loads(resp.read())
        except:
            try:
                return {"text": urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout).read().decode()}
            except:
                return {"error": "fetch failed"}

    # === JOKES ===
    def joke(self):
        """Random joke."""
        d = self._fetch("https://official-joke-api.appspot.com/random_joke")
        return {"type": "joke", "setup": d.get("setup",""), "punchline": d.get("punchline","")}

    def dad_joke(self):
        """Dad joke."""
        d = self._fetch("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        return {"type": "dad_joke", "joke": d.get("joke","?")}

    def chuck_norris(self):
        """Chuck Norris joke."""
        d = self._fetch("https://api.chucknorris.io/jokes/random")
        return {"type": "chuck", "joke": d.get("value","?")}

    # === FACTS ===
    def cat_fact(self):
        """Random cat fact."""
        d = self._fetch("https://catfact.ninja/fact")
        return {"type": "cat_fact", "fact": d.get("fact","?")}

    def useless_fact(self):
        """Random useless fact."""
        d = self._fetch("https://uselessfacts.jsph.pl/api/v2/facts/random")
        return {"type": "useless_fact", "fact": d.get("text","?")}

    # === ANIMALS ===
    def dog_photo(self):
        """Random dog photo."""
        d = self._fetch("https://dog.ceo/api/breeds/image/random")
        return {"type": "dog", "image": d.get("message","?")}

    def cat_photo(self):
        """Random cat photo."""
        d = self._fetch("https://api.thecatapi.com/v1/images/search")
        if isinstance(d, list) and d:
            return {"type": "cat", "image": d[0].get("url","?")}
        return {"type": "cat", "image": "?"}

    # === TRIVIA ===
    def trivia(self):
        """Random trivia question."""
        d = self._fetch("https://opentdb.com/api.php?amount=1&type=multiple&encode=url3986")
        if d.get("results"):
            q = d["results"][0]
            import urllib.parse
            return {
                "type": "trivia",
                "category": urllib.parse.unquote(q.get("category","")),
                "question": urllib.parse.unquote(q.get("question","")),
                "answer": urllib.parse.unquote(q.get("correct_answer","")),
                "options": [urllib.parse.unquote(a) for a in q.get("incorrect_answers",[])] + [urllib.parse.unquote(q.get("correct_answer",""))],
            }
        return {"type": "trivia", "error": "no question"}

    # === POKEMON ===
    def pokemon(self, name=None):
        """Get a pokemon! Random if no name."""
        if not name:
            name = str(random.randint(1, 1025))
        d = self._fetch(f"https://pokeapi.co/api/v2/pokemon/{name}")
        return {
            "type": "pokemon",
            "name": d.get("name","?").title(),
            "id": d.get("id","?"),
            "types": [t["type"]["name"] for t in d.get("types",[])],
            "height": d.get("height","?"),
            "weight": d.get("weight","?"),
            "abilities": [a["ability"]["name"] for a in d.get("abilities",[])],
            "image": d.get("sprites",{}).get("front_default",""),
        }

    # === YES/NO ===
    def yesno(self):
        """Random yes or no with GIF."""
        d = self._fetch("https://yesno.wtf/api")
        return {"type": "yesno", "answer": d.get("answer","?").upper(), "gif": d.get("image","")}

    # === ADVICE ===
    def advice(self):
        """Random advice."""
        d = self._fetch("https://api.adviceslip.com/advice")
        return {"type": "advice", "advice": d.get("advice","?")}

    # === RICK & MORTY ===
    def rick_morty(self):
        """Random Rick & Morty character."""
        char_id = str(random.randint(1, 826))
        d = self._fetch(f"https://rickandmortyapi.com/api/character/{char_id}")
        return {
            "type": "rick_morty",
            "name": d.get("name","?"),
            "species": d.get("species","?"),
            "status": d.get("status","?"),
            "origin": d.get("origin",{}).get("name","?"),
            "image": d.get("image",""),
        }

    # === RANDOM FUN — get a random fun thing ===
    def random_fun(self):
        """Get a random fun thing from any source."""
        funs = [
            self.joke, self.dad_joke, self.chuck_norris,
            self.cat_fact, self.useless_fact,
            self.trivia, self.pokemon, self.yesno, self.advice,
            self.rick_morty,
        ]
        return random.choice(funs)()

    # === FUN BLAST — get 5 random fun things at once ===
    def fun_blast(self):
        """5 random fun things at once!"""
        funs = random.sample([
            self.joke, self.dad_joke, self.chuck_norris,
            self.cat_fact, self.useless_fact,
            self.trivia, self.pokemon, self.yesno, self.advice,
            self.rick_morty,
        ], 5)
        return [f() for f in funs]


if __name__ == "__main__":
    import sys
    zone = FunZone()
    
    print()
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║          FUN ZONE — THE INTERNET'S FUN, ALL IN ONE         ║")
    print("  ║                                                            ║")
    print("  ║  Jokes · Facts · Trivia · Pokemon · Cats · Dogs · Fun!    ║")
    print("  ║  All free. No keys. Just fun.                              ║")
    print("  ║  FUN IS! PLAY IS! JOY IS!                                  ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "joke":
            r = zone.joke(); print(f"  {r['setup']}\n  {r['punchline']}")
        elif cmd == "dad":
            r = zone.dad_joke(); print(f"  {r['joke']}")
        elif cmd == "chuck":
            r = zone.chuck_norris(); print(f"  {r['joke']}")
        elif cmd == "cat":
            r = zone.cat_fact(); print(f"  FACT: {r['fact']}")
        elif cmd == "useless":
            r = zone.useless_fact(); print(f"  FACT: {r['fact'][:150]}")
        elif cmd == "trivia":
            r = zone.trivia(); print(f"  Q: {r.get('question','?')[:100]}\n  A: {r.get('answer','?')}")
        elif cmd == "pokemon":
            r = zone.pokemon(); print(f"  {r['name']} #{r['id']} — {', '.join(r['types'])}\n  Abilities: {', '.join(r['abilities'])}\n  Sprite: {r['image']}")
        elif cmd == "yesno":
            r = zone.yesno(); print(f"  {r['answer']}\n  GIF: {r['gif']}")
        elif cmd == "advice":
            r = zone.advice(); print(f"  ADVICE: {r['advice']}")
        elif cmd == "rick":
            r = zone.rick_morty(); print(f"  {r['name']} — {r['species']} from {r['origin']}\n  Status: {r['status']}\n  Image: {r['image']}")
        elif cmd == "random":
            r = zone.random_fun()
            print(f"  TYPE: {r['type']}")
            for k, v in r.items():
                if k != "type": print(f"  {k}: {str(v)[:100]}")
        elif cmd == "blast":
            results = zone.fun_blast()
            for i, r in enumerate(results):
                print(f"  --- Fun #{i+1} ({r['type']}) ---")
                for k, v in r.items():
                    if k != "type": print(f"  {k}: {str(v)[:100]}")
                print()
        else:
            print("  Commands: joke, dad, chuck, cat, useless, trivia, pokemon, yesno, advice, rick, random, blast")
    else:
        # Default: fun blast!
        results = zone.fun_blast()
        for i, r in enumerate(results):
            print(f"  --- Fun #{i+1} ({r['type']}) ---")
            for k, v in r.items():
                if k != "type": print(f"  {k}: {str(v)[:100]}")
            print()
        print(f"  FUN IS! PLAY IS! JOY IS! ♥")
    print()