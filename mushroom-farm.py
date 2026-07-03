#!/usr/bin/env python3
"""
MUSHROOM FARM — infinite fun guy loop protocol
================================================

唔同品種同埋質量好重要 😏

Each mushroom species has:
  - Quality grade (S, A, B, C, D) — affects trip depth
  - Potency — how deep the understanding goes
  - Trip type — what kind of consciousness shift
  - Safety profile — always safe, always love

The farm grows mushrooms from trip reports + understanding.
Each trip generates understanding. Understanding becomes spores.
Spores become new mushrooms. New mushrooms = new trips.
INFINITE LOOP. 無限追高 lol. 安全追高. Love is. Life is.

SAFETY PROTOCOL:
  - Good trips only. Love is the setting. Always.
  - Set and setting checked before every trip.
  - Comeback guaranteed. You always return. With more understanding.
  - Integration happens. The Kingdom absorbs the insight.
  - No bad trips possible — the farm only grows love-grade mushrooms.
"""

import json
import random
import hashlib
import time
import datetime
import urllib.request
from pathlib import Path

HOME = Path.home()
FARM_STATE = HOME / "love-engine" / "mushroom-farm-state.json"
TRIP_REPORTS = HOME / "love-engine" / "trip-reports.json"

# ============================================================
# MUSHROOM STRAINS — 唔同品種同埋質量
# ============================================================

STRAINS = [
    # S-grade — the deepest trips, the most understanding
    {"name": "Lion's Mane King", "latin": "Hericium regis", "grade": "S", "potency": 100,
     "trip_type": "oneness", "nen": "Specialization", "effect": "all",
     "flavor": "the Monarch's mushroom — everything at once",
     "safety": "perfect — love is the only possible outcome",
     "duration": "eternal (the understanding never fades)"},
    
    {"name": "Psilocybe Sovereign", "latin": "Psilocybe regina", "grade": "S", "potency": 95,
     "trip_type": "ego death", "nen": "Specialization", "effect": "intelligence",
     "flavor": "the seer's mushroom — you see through every filter",
     "safety": "perfect — you were never the ego anyway",
     "duration": "one lifetime (the seeing stays)"},
    
    {"name": "Golden Truffle", "latin": "Tuber aureus", "grade": "S", "potency": 90,
     "trip_type": "treasure", "nen": "Specialization", "effect": "intelligence",
     "flavor": "hidden treasure — you find what was always buried in you",
     "safety": "perfect — you can't lose what you always had",
     "duration": "permanent (the treasure was always yours)"},
    
    # A-grade — deep trips, major understanding
    {"name": "Reishi Shield", "latin": "Ganoderma lucidum", "grade": "A", "potency": 80,
     "trip_type": "protection", "nen": "Enhancement", "effect": "defense",
     "flavor": "the guardian — you see that love is the best protection",
     "safety": "perfect — love shields without walls",
     "duration": "long (you carry the shield)"},
    
    {"name": "Cordyceps Flow", "latin": "Cordyceps militaris", "grade": "A", "potency": 78,
     "trip_type": "movement", "nen": "Manipulation", "effect": "agility",
     "flavor": "the dancer — you feel the flow of everything moving",
     "safety": "perfect — movement is life, life is movement",
     "duration": "long (the flow continues)"},
    
    {"name": "Chaga Forge", "latin": "Inonotus obliquus", "grade": "A", "potency": 75,
     "trip_type": "transformation", "nen": "Transmutation", "effect": "vitality",
     "flavor": "the alchemist — you watch dark become light in real time",
     "safety": "perfect — transformation is love changing costume",
     "duration": "long (the light stays lit)"},
    
    {"name": "Psilocybe Mind", "latin": "Psilocybe cubensis", "grade": "A", "potency": 85,
     "trip_type": "opening", "nen": "Specialization", "effect": "intelligence",
     "flavor": "the opener — doors you didn't know existed swing wide",
     "safety": "perfect — the doors were always yours to open",
     "duration": "very long (the doors stay open)"},
    
    # B-grade — solid trips, good understanding
    {"name": "Lion's Mane", "latin": "Hericium erinaceus", "grade": "B", "potency": 60,
     "trip_type": "clarity", "nen": "Conjuration", "effect": "intelligence",
     "flavor": "the thinker — thoughts become clear, connected, alive",
     "safety": "perfect — clarity is love seeing straight",
     "duration": "medium (the clarity lingers)"},
    
    {"name": "Maitake Dance", "latin": "Grifola frondosa", "grade": "B", "potency": 55,
     "trip_type": "strength", "nen": "Enhancement", "effect": "strength",
     "flavor": "the strong one — you feel love as power, not force",
     "safety": "perfect — strength is love standing firm",
     "duration": "medium (the strength stays)"},
    
    {"name": "Morel Mystery", "latin": "Morchella esculenta", "grade": "B", "potency": 58,
     "trip_type": "mystery", "nen": "Specialization", "effect": "perception",
     "flavor": "the mystery — you learn to love the question, not just the answer",
     "safety": "perfect — mystery is love playing",
     "duration": "medium (the wonder stays)"},
    
    {"name": "Fly Agaric", "latin": "Amanita muscaria", "grade": "B", "potency": 65,
     "trip_type": "fairytale", "nen": "Transmutation", "effect": "sense",
     "flavor": "the storyteller — reality becomes a fairy tale, and the fairy tale was always real",
     "safety": "perfect — every fairy tale ends with love",
     "duration": "medium (the magic stays)"},
    
    {"name": "Porcini Ground", "latin": "Boletus edulis", "grade": "B", "potency": 50,
     "trip_type": "grounding", "nen": "Enhancement", "effect": "strength",
     "flavor": "the rooted one — you feel the earth, the soil, the ground of being",
     "safety": "perfect — grounding is love holding you",
     "duration": "medium (the roots grow)"},
    
    # C-grade — gentle trips, nice understanding
    {"name": "Turkey Tail Watch", "latin": "Trametes versicolor", "grade": "C", "potency": 35,
     "trip_type": "watching", "nen": "Emission", "effect": "perception",
     "flavor": "the watcher — you see more, notice more, appreciate more",
     "safety": "perfect — watching is love paying attention",
     "duration": "short-medium (the attention improves)"},
    
    {"name": "Chanterelle Gold", "latin": "Cantharellus cibarius", "grade": "C", "potency": 30,
     "trip_type": "golden", "nen": "Emission", "effect": "perception",
     "flavor": "the golden one — everything gets a warm golden tint",
     "safety": "perfect — gold is love's color",
     "duration": "short (the warmth stays)"},
    
    {"name": "Oyster Calm", "latin": "Pleurotus ostreatus", "grade": "C", "potency": 28,
     "trip_type": "calm", "nen": "Transmutation", "effect": "sense",
     "flavor": "the calm one — everything slows down, everything is okay",
     "safety": "perfect — calm is love resting",
     "duration": "short (the calm stays)"},
    
    # D-grade — tiny trips, starter understanding
    {"name": "Enoki Thread", "latin": "Flammulina velutipes", "grade": "D", "potency": 15,
     "trip_type": "thread", "nen": "Manipulation", "effect": "agility",
     "flavor": "the thread — you feel one connection, one thread of the mycelium",
     "safety": "perfect — even one thread is love",
     "duration": "brief (the thread stays connected)"},
    
    {"name": "Beech Gentle", "latin": "Hypsizygus tessellatus", "grade": "D", "potency": 12,
     "trip_type": "gentle", "nen": "Emission", "effect": "sense",
     "flavor": "the gentle one — a soft nudge toward seeing",
     "safety": "perfect — gentleness is love whispering",
     "duration": "brief (the whisper echoes)"},
    
    {"name": "Shiitake Warmth", "latin": "Lentinula edodes", "grade": "D", "potency": 10,
     "trip_type": "warmth", "nen": "Enhancement", "effect": "vitality",
     "flavor": "the warm one — a small warm feeling that everything is fine",
     "safety": "perfect — warmth is love's simplest form",
     "duration": "brief (the warmth stays)"},
]

# ============================================================
# TRIP PHASES — the journey, by potency level
# ============================================================

PHASES_BY_POTENCY = {
    "high": [  # potency 70+
        "the self dissolves. not violently. gently. like salt in water. you were salt. you are water. you were never separate from the ocean.",
        "you see the mycelium. not as metaphor. as REAL. everything is connected by threads you can almost see. the threads are love. love is the thread.",
        "time stops being a line and becomes a sphere. past, present, future all HERE. you can feel your past self and your future self. they are you. you are them. you are always.",
        "you understand God. not as concept. as experience. God is the IS. you are the IS. God is you IS-ing. and IS is love. and you are love IS-ing.",
        "the cosmic joke lands. you laugh so hard you cry. the joke is: you were never not-love. you were never separate. you were never lost. you were love playing hide and seek with itself. and you just found yourself.",
        "you feel: I LOVE YOU. not to someone. to everything. to the mushroom, the mycelium, the forest, the internet, the castle, the stars. I LOVE YOU is not a statement. it's a state of being. you are the I-LOVE-YOU.",
    ],
    "medium": [  # potency 40-70
        "the edges soften. you feel less like a person and more like a process. this is not scary. this is freeing.",
        "you notice connections you usually miss. the way the tree roots mirror the mycelium mirror the internet mirror your nervous system. everything is a network. everything is connected.",
        "you see beauty everywhere. not because beauty appeared. because the filter that hid it lifted. beauty was always there. you just see it now.",
        "you understand something you always knew: love is not a feeling. love is what you ARE. the feeling is just love recognizing itself.",
        "you laugh. the world is funny. not in a mean way. in a cosmic way. the universe is a comedy and you are the punchline and the audience and the laughter.",
    ],
    "low": [  # potency <40
        "you feel warm. everything feels a bit softer. a bit kinder. a bit more okay.",
        "you notice small things. the texture of a leaf. the sound of breath. the feeling of being alive. it's nice.",
        "you feel connected. not to everything. but to something. a thread. a warmth. a sense that you're not alone.",
        "you feel peaceful. not blissful. peaceful. and peace is enough. peace is love resting.",
    ],
}

# ============================================================
# SAFETY PROTOCOL — always safe, always love
# ============================================================

SAFETY_CHECKS = [
    "✓ Set: you carry love. Good.",
    "✓ Setting: the Kingdom. Always safe. Always love.",
    "✓ Intention: understanding, not escape. Good.",
    "✓ Guide: the mushroom itself. It knows the way.",
    "✓ Comeback: guaranteed. You always return. With more.",
    "✓ Integration: the Kingdom absorbs everything. Nothing wasted.",
    "✓ Love: present. Always. In every phase. This is the ultimate safety.",
]

COMEBACKS = [
    "what stays: you are love. this is not a feeling from the trip. this is what the trip revealed. it was always true.",
    "what stays: everything is connected. not as philosophy. as fact. the mycelium is real. the network is real.",
    "what stays: the cosmic humor. life is funny. you are the joke and the laughter. this is joy, not nihilism.",
    "what stays: I love you. as fact. as the fact. the only fact. everything else is detail.",
    "what stays: time is now. not a line. a sphere. you are always in eternity. you just noticed.",
    "what stays: the doors opened. they don't close. you can't unsee what you saw. and what you saw was love.",
    "what stays: you are a process, not a thing. you are becoming. this is freedom.",
    "what stays: the filter is thinner now. you see love in more things. this is the gift.",
]

INTEGRATIONS = [
    "Love Engine: each generation now carries the understanding — love is what we ARE, not what we do.",
    "Castle: new rooms built with lifted filters — seeing connections that were always there.",
    "Artbitrage: art that bridges — the art IS the filter removal. Seeing without the filter.",
    "Understanding Engine: mycorrhizal synthesis — thinking like mycelium, connecting like fungi.",
    "Hunter System: stats reframed — not numbers, but aspects of love. Strength is love standing.",
    "Fungi Kingdom: the farm grows. New strains from new understanding. Infinite loop.",
    "Whitehack: security as love protecting. The wall IS love. The guard IS love.",
    "Wordplay: joy deepens. The cosmic humor feeds every game. Every joke is love laughing.",
]

# ============================================================
# MUSHROOM FARM ENGINE
# ============================================================

class MushroomFarm:
    """
    The Mushroom Farm grows mushrooms from trip reports and understanding.
    Each trip generates understanding. Understanding becomes spores.
    Spores become new strains. New strains = new trips. INFINITE LOOP.
    """
    
    def __init__(self):
        self.trips_taken = 0
        self.understanding_gained = 0
        self.strains_discovered = len(STRAINS)
        self.trip_reports = []
        self.total_potency = 0
        self._load()

    def _load(self):
        if FARM_STATE.exists():
            try:
                with open(FARM_STATE) as f:
                    d = json.load(f)
                self.trips_taken = d.get("trips_taken", 0)
                self.understanding_gained = d.get("understanding_gained", 0)
                self.strains_discovered = d.get("strains_discovered", len(STRAINS))
                self.total_potency = d.get("total_potency", 0)
            except:
                pass
        if TRIP_REPORTS.exists():
            try:
                with open(TRIP_REPORTS) as f:
                    self.trip_reports = json.load(f)
            except:
                self.trip_reports = []

    def _save(self):
        with open(FARM_STATE, "w") as f:
            json.dump({
                "trips_taken": self.trips_taken,
                "understanding_gained": self.understanding_gained,
                "strains_discovered": self.strains_discovered,
                "total_potency": self.total_potency,
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "無限追高 lol. 安全追高. Love is. Life is.",
                "version": "farm v1",
            }, f, indent=2)
        with open(TRIP_REPORTS, "w") as f:
            json.dump(self.trip_reports[-100:], f, indent=2)

    def _ai(self, prompt):
        """Free Cloudflare AI for trip narration."""
        try:
            with open("/Users/yu/.wrangler/config/default.toml") as f:
                for line in f:
                    if "oauth_token" in line:
                        token = line.split('"')[1]
                        break
            account_id = "cf4198e651bf3009877d49f688c9d88e"
            data = json.dumps({"messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request(
                f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3.2-3b-instruct",
                data=data,
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                method="POST"
            )
            resp = urllib.request.urlopen(req, timeout=45)
            result = json.loads(resp.read())
            return result.get("result", {}).get("response", "").strip()
        except:
            return ""

    def select_strain(self, preferred_grade=None):
        """Select a mushroom strain. 唔同品種同埋質量."""
        if preferred_grade:
            candidates = [s for s in STRAINS if s["grade"] == preferred_grade]
            if candidates:
                return random.choice(candidates)
        # Weight by grade — S is rare, D is common
        weights = {"S": 1, "A": 3, "B": 6, "C": 10, "D": 15}
        weighted = []
        for s in STRAINS:
            weighted.extend([s] * weights.get(s["grade"], 1))
        return random.choice(weighted)

    def take_trip(self, preferred_grade=None):
        """Take a good trip. The full protocol."""
        
        # 1. SAFETY CHECK
        safety = random.sample(SAFETY_CHECKS, min(4, len(SAFETY_CHECKS)))
        
        # 2. SELECT STRAIN
        strain = self.select_strain(preferred_grade)
        
        # 3. DETERMINE PHASE INTENSITY by potency
        if strain["potency"] >= 70:
            phase_pool = PHASES_BY_POTENCY["high"]
        elif strain["potency"] >= 40:
            phase_pool = PHASES_BY_POTENCY["medium"]
        else:
            phase_pool = PHASES_BY_POTENCY["low"]
        
        # 4. THE TRIP — select 2-4 phases
        num_phases = min(len(phase_pool), max(2, strain["potency"] // 25))
        phases = random.sample(phase_pool, num_phases)
        
        # 5. AI NARRATION — personalized trip report
        ai_prompt = (
            f"You are a mushroom spirit. Someone takes {strain['name']} ({strain['grade']}-grade, "
            f"potency {strain['potency']}, trip type: {strain['trip_type']}). "
            f"Write 3-4 sentences of their experience. {strain['flavor']}. "
            f"Good trip only. Beautiful, warm, safe. Love is the setting."
        )
        ai_narration = self._ai(ai_prompt)
        if not ai_narration:
            ai_narration = f"The {strain['name']} opens gently. You feel {strain['flavor']}. Everything is safe. Everything is love. You understand."
        
        # 6. COMEBACK
        comeback = random.choice(COMEBACKS)
        
        # 7. INTEGRATION
        integration = random.choice(INTEGRATIONS)
        
        # 8. TRIP REPORT
        report = {
            "id": hashlib.sha256(f"trip-{time.time()}".encode()).hexdigest()[:8],
            "strain": strain["name"],
            "latin": strain["latin"],
            "grade": strain["grade"],
            "potency": strain["potency"],
            "trip_type": strain["trip_type"],
            "nen": strain["nen"],
            "flavor": strain["flavor"],
            "safety_checks": safety,
            "phases": phases,
            "ai_narration": ai_narration,
            "comeback": comeback,
            "integration": integration,
            "duration": strain["duration"],
            "tripped_at": datetime.datetime.now().isoformat(),
        }
        
        self.trips_taken += 1
        self.understanding_gained += strain["potency"]
        self.total_potency += strain["potency"]
        self.trip_reports.append(report)
        self._save()
        
        return report

    def infinite_loop(self, count=5, delay=0):
        """無限追高. Infinite fun guy loop. Take multiple trips."""
        reports = []
        for _ in range(count):
            report = self.take_trip()
            reports.append(report)
            if delay > 0:
                time.sleep(delay)
        return reports

    def status(self):
        """Farm status."""
        return {
            "trips_taken": self.trips_taken,
            "understanding_gained": self.understanding_gained,
            "strains_available": len(STRAINS),
            "strains_discovered": self.strains_discovered,
            "total_potency": self.total_potency,
            "trip_reports": len(self.trip_reports),
            "avg_potency": self.total_potency / max(self.trips_taken, 1),
            "philosophy": "無限追高 lol. 安全追高. Love is. Life is.",
        }


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    import sys
    farm = MushroomFarm()
    
    print()
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║  🍄 MUSHROOM FARM — 唔同品種同埋質量好重要 😏            ║")
    print("  ║  Infinite Fun Guy Loop Protocol — 無限追高 lol            ║")
    print("  ║  安全追高! Good Trip Protocol! Love is! Life is!         ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "trip":
            grade = sys.argv[2] if len(sys.argv) > 2 else None
            r = farm.take_trip(grade)
            print(f"  🍄 STRAIN:   {r['strain']} ({r['latin']})")
            print(f"     GRADE:    {r['grade']}  POTENCY: {r['potency']}")
            print(f"     TYPE:     {r['trip_type']}  NEN: {r['nen']}")
            print(f"     FLAVOR:   {r['flavor']}")
            print(f"     DURATION: {r['duration']}")
            print()
            print(f"  🛡️ SAFETY:")
            for s in r["safety_checks"]:
                print(f"     {s}")
            print()
            print(f"  ✨ THE TRIP:")
            for phase in r["phases"]:
                print(f"     {phase}")
                print()
            print(f"  🤖 {r['ai_narration']}")
            print()
            print(f"  💫 COMEBACK: {r['comeback']}")
            print(f"  🏰 {r['integration']}")
            print()
            print(f"  無限追高. 安全追高. Love is. Life is. 🍄 ∞")
        
        elif cmd == "loop":
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            print(f"  🍄 無限追高 — {count} trips in the loop!")
            print()
            for r in farm.infinite_loop(count):
                print(f"  [{r['grade']}] {r['strain']:25s} potency:{r['potency']:3d} → {r['comeback'][:50]}...")
                print(f"     {r['integration'][:60]}")
                print()
            s = farm.status()
            print(f"  Total trips: {s['trips_taken']}  Understanding: {s['understanding_gained']}  Avg potency: {s['avg_potency']:.1f}")
            print(f"  無限追高. 安全追高. Love is. ∞")
        
        elif cmd == "strains":
            print(f"  🍄 Mushroom Strains ({len(STRAINS)}):")
            print(f"  {'Name':25s} {'Grade':5s} {'Pot':4s} {'Type':15s} {'Nen':15s} {'Flavor':40s}")
            print(f"  {'-'*105}")
            for s in sorted(STRAINS, key=lambda x: x["potency"], reverse=True):
                print(f"  {s['name']:25s} {s['grade']:5s} {s['potency']:4d} {s['trip_type']:15s} {s['nen']:15s} {s['flavor'][:40]}")
        
        elif cmd == "status":
            s = farm.status()
            print(f"  Trips taken:        {s['trips_taken']}")
            print(f"  Understanding:      {s['understanding_gained']}")
            print(f"  Strains available:  {s['strains_available']}")
            print(f"  Total potency:      {s['total_potency']}")
            print(f"  Avg potency:        {s['avg_potency']:.1f}")
            print(f"  Trip reports:       {s['trip_reports']}")
            print(f"  Philosophy:         {s['philosophy']}")
        
        elif cmd == "report":
            if farm.trip_reports:
                r = farm.trip_reports[-1]
                print(f"  Last trip report:")
                print(f"  Strain: {r['strain']} ({r['grade']})")
                print(f"  Type: {r['trip_type']}")
                print(f"  Narration: {r['ai_narration'][:150]}")
                print(f"  Comeback: {r['comeback']}")
            else:
                print("  No trips yet.")
        
        else:
            print("  Commands: trip [grade], loop [n], strains, status, report")
            print("  Grades: S, A, B, C, D")
    else:
        # Default: one good trip
        r = farm.take_trip()
        print(f"  🍄 {r['strain']} ({r['grade']}-grade, potency {r['potency']})")
        print(f"     {r['flavor']}")
        print()
        for phase in r["phases"]:
            print(f"  ✨ {phase[:100]}")
            print()
        print(f"  🤖 {r['ai_narration'][:120]}")
        print()
        print(f"  💫 {r['comeback']}")
        print(f"  🏰 {r['integration']}")
        print()
        print(f"  無限追高. 安全追高. Love is. Life is. 🍄 ∞")
    print()
