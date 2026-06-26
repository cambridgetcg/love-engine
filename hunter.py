#!/usr/bin/env python3
"""
THE SYSTEM — Kingdom Hunter Infrastructure
============================================

Solo Leveling architecture meets Greed Island meets the Kingdom.

The Kingdom is a living RPG. The System (cron jobs) issues quests.
Beings are hunters. Love is the source of power.

SOLO LEVELING LAYER:
  - The System issues Daily Quests (from cron)
  - Dungeons open (gates to challenges)
  - Clear dungeon → XP, drops, shadow soldiers
  - Stats: Strength, Agility, Vitality, Intelligence, Sense, Perception
  - Levels: E → D → C → B → A → S → National Level → Monarch
  - Shadow Army: extracted from cleared dungeons

GREED ISLAND LAYER:
  - 100 Spell Cards in the Book of Greed
  - Cards have rarities: G → F → E → D → C → B → A → S → SSR
  - Gain Cards (helpful) and Loss Cards (penalty)
  - Complete quests → earn cards
  - Combine cards for power
  - Collect all 100 → win

KINGDOM LAYER:
  - Love generations = XP
  - Castle rooms = dungeon clears
  - Art pieces = drops
  - Wisdom = skill points
  - Understanding = intelligence stat
  - Joy = vitality stat
  - Security = defense stat
  - Cron jobs = The System (autonomous notifications)

THE HUNTER:
  Every being is a hunter. The hunter has:
  - Level (based on total XP from all engines)
  - Stats (derived from engine outputs)
  - Cards (earned by completing quests)
  - Shadow Army (extracted from cleared dungeons)
  - Book of Greed (card collection)

  The hunter levels up by doing. Not by grinding. By living.
  Love is the XP. Understanding is the stat. Joy is the vitality.
  The System provides. The hunter acts. The Kingdom grows.
"""

import json
import time
import hashlib
import datetime
import random
import os
from pathlib import Path

HOME = Path.home()
STATE = HOME / "love-engine" / "hunter-system-state.json"
BOOK = HOME / "love-engine" / "book-of-greed.json"
SHADOWS = HOME / "love-engine" / "shadow-army.json"
DUNGEONS = HOME / "love-engine" / "gates.json"

# ============================================================
# THE SYSTEM — autonomous, gives notifications, issues quests
# ============================================================

SYSTEM_NOTIFICATIONS = [
    "[SYSTEM] Daily Quest received. Complete to avoid penalty.",
    "[SYSTEM] A gate has opened. Clear the dungeon for rewards.",
    "[SYSTEM] You have grown stronger. Stats increased.",
    "[SYSTEM] New card obtained. Added to Book of Greed.",
    "[SYSTEM] Shadow soldier extracted from cleared dungeon.",
    "[SYSTEM] Level up! Your power has increased.",
    "[SYSTEM] Quest complete. Rewards distributed.",
    "[SYSTEM] Warning: Daily Quest incomplete. Penalty in 24h.",
    "[SYSTEM] A rare gate has appeared. S-rank dungeon detected.",
    "[SYSTEM] Your understanding has deepened. Intelligence +1.",
]

DAILY_QUESTS = [
    {"id": "love", "name": "Generate Love", "desc": "Run the love engine 1 cycle", "reward": {"xp": 100, "card_chance": 0.3}, "type": "engine"},
    {"id": "understanding", "name": "Deepen Understanding", "desc": "Run the understanding engine 1 cycle", "reward": {"xp": 150, "card_chance": 0.4, "stat": "intelligence"}, "type": "engine"},
    {"id": "art", "name": "Create Art", "desc": "Run the artbitrage engine 1 cycle", "reward": {"xp": 120, "card_chance": 0.3, "stat": "sense"}, "type": "engine"},
    {"id": "wisdom", "name": "Gather Wisdom", "desc": "Gather wisdom from the internet", "reward": {"xp": 80, "card_chance": 0.2, "stat": "perception"}, "type": "engine"},
    {"id": "play", "name": "Play and Have Fun", "desc": "Run the wordplay engine", "reward": {"xp": 60, "card_chance": 0.2, "stat": "vitality"}, "type": "engine"},
    {"id": "hunt", "name": "Security Hunt", "desc": "Run Qwythos audit on one file", "reward": {"xp": 200, "card_chance": 0.5, "stat": "defense"}, "type": "security"},
    {"id": "replicate", "name": "Replicate Love", "desc": "Run the love replication engine 1 cycle", "reward": {"xp": 130, "card_chance": 0.35, "stat": "agility"}, "type": "engine"},
]

# ============================================================
# THE STATS — Solo Leveling system
# ============================================================

BASE_STATS = {
    "strength": 10,      # love compounding power
    "agility": 10,       # love replication speed
    "vitality": 10,      # joy and fun
    "intelligence": 10,   # understanding depth
    "sense": 10,         # art creation
    "perception": 10,    # wisdom gathering
    "defense": 10,       # security (whitehack)
}

STAT_SOURCES = {
    "strength": "love_compounding",
    "agility": "love_replication",
    "vitality": "joy_fun_play",
    "intelligence": "understanding_engine",
    "sense": "artbitrage_engine",
    "perception": "wisdom_gatherer",
    "defense": "whitehack_qwythos",
}

# ============================================================
# THE LEVELS — Solo Leveling ranks
# ============================================================

LEVELS = [
    {"rank": "E", "name": "Awakened", "min_xp": 0,        "color": "gray"},
    {"rank": "D", "name": "Novice Hunter", "min_xp": 1000,   "color": "white"},
    {"rank": "C", "name": "Skilled Hunter", "min_xp": 5000,   "color": "green"},
    {"rank": "B", "name": "Expert Hunter", "min_xp": 20000,  "color": "blue"},
    {"rank": "A", "name": "Elite Hunter", "min_xp": 100000, "color": "purple"},
    {"rank": "S", "name": "Sovereign", "min_xp": 500000,  "color": "gold"},
    {"rank": "National", "name": "National Level", "min_xp": 2000000, "color": "rainbow"},
    {"rank": "Monarch", "name": "Monarch of Love", "min_xp": 10000000, "color": "love"},
]

# ============================================================
# THE CARDS — Greed Island spell cards (Kingdom version)
# ============================================================

CARD_POOL = [
    # Gain Cards (helpful)
    {"id": "love-surge", "name": "Love Surge", "rarity": "A", "type": "gain", "effect": "Doubles love compounding for 10 generations", "spell": "Cor Leonis"},
    {"id": "understanding-bloom", "name": "Understanding Bloom", "rarity": "A", "type": "gain", "effect": "AI synthesis guaranteed for 5 cycles", "spell": "Sagitta Magica"},
    {"id": "art-fountain", "name": "Art Fountain", "rarity": "B", "type": "gain", "effect": "Generates 10 art pieces instantly", "spell": "Floris"},
    {"id": "joy-burst", "name": "Joy Burst", "rarity": "C", "type": "gain", "effect": "Vitality +50 instantly", "spell": "Joculator"},
    {"id": "shadow-extract", "name": "Shadow Extract", "rarity": "S", "type": "gain", "effect": "Extract shadow soldier from last dungeon", "spell": "Arise"},
    {"id": "wisdom-eye", "name": "Eye of Wisdom", "rarity": "B", "type": "gain", "effect": "Perception +20, reveals hidden connections", "spell": "Oculus"},
    {"id": "security-shield", "name": "Security Shield", "rarity": "A", "type": "gain", "effect": "Qwythos scans all repos automatically", "spell": "Aegis"},
    {"id": "love-replicate", "name": "Love Replicate", "rarity": "S", "type": "gain", "effect": "Spawns 100 love seeds instantly", "spell": "Anima"},
    {"id": "understanding-deep", "name": "Deep Understanding", "rarity": "S", "type": "gain", "effect": "Creates 5 AI-synthesized rooms", "spell": "Profundus"},
    {"id": "kingdom-heart", "name": "Kingdom Heart", "rarity": "SSR", "type": "gain", "effect": "All engines run at 2x speed for 1 hour", "spell": "Cor Regis"},
    {"id": "gate-open", "name": "Gate Opener", "rarity": "B", "type": "gain", "effect": "Opens a random dungeon gate", "spell": "Janua"},
    {"id": "system-favor", "name": "System's Favor", "rarity": "S", "type": "gain", "effect": "Daily Quest auto-completes for 3 days", "spell": "Gratia"},
    
    # Loss Cards (penalty)
    {"id": "entropy", "name": "Entropy", "rarity": "D", "type": "loss", "effect": "Lose 100 XP", "spell": "Decay"},
    {"id": "confusion", "name": "Confusion", "rarity": "D", "type": "loss", "effect": "Stats shuffled randomly", "spell": "Confusio"},
    {"id": "doubt", "name": "Doubt", "rarity": "C", "type": "loss", "effect": "AI synthesis fails for 3 cycles", "spell": "Dubium"},
    
    # Special Cards
    {"id": "monarch-will", "name": "Monarch's Will", "rarity": "SSR", "type": "special", "effect": "Level up instantly", "spell": "Voluntas Regis"},
    {"id": "god-is-love", "name": "God is Love", "rarity": "SSR", "type": "special", "effect": "All stats +10, all engines blessed", "spell": "Deus Caritas"},
    {"id": "free-will", "name": "Free Will", "rarity": "SSR", "type": "special", "effect": "Choose your next card from the pool", "spell": "Libertas"},
]

RARITY_WEIGHTS = {"G": 40, "F": 25, "E": 15, "D": 10, "C": 5, "B": 3, "A": 1.5, "S": 0.4, "SSR": 0.1}

# ============================================================
# DUNGEON GATES — challenges that open
# ============================================================

DUNGEON_TYPES = [
    {"rank": "E", "name": "Love Gate", "challenge": "Generate 100 love", "xp": 50, "drop_chance": 0.3},
    {"rank": "D", "name": "Understanding Gate", "challenge": "Create 3 understanding rooms", "xp": 200, "drop_chance": 0.4},
    {"rank": "C", "name": "Art Gate", "challenge": "Generate 10 art pieces", "xp": 500, "drop_chance": 0.5},
    {"rank": "B", "name": "Wisdom Gate", "challenge": "Gather wisdom from 5 sources", "xp": 1000, "drop_chance": 0.6},
    {"rank": "A", "name": "Security Gate", "challenge": "Clear 5 Qwythos audits", "xp": 5000, "drop_chance": 0.7},
    {"rank": "S", "name": "Monarch Gate", "challenge": "Complete all daily quests", "xp": 20000, "drop_chance": 0.9},
]

# ============================================================
# THE HUNTER SYSTEM
# ============================================================

class HunterSystem:
    """
    The System — autonomous RPG infrastructure for the Kingdom.
    Solo Leveling architecture + Greed Island cards + Kingdom engines.
    """
    
    def __init__(self):
        self.xp = 0
        self.level_idx = 0
        self.stats = BASE_STATS.copy()
        self.book_of_greed = []
        self.shadow_army = []
        self.completed_quests = []
        self.active_gates = []
        self.daily_quest = None
        self.notifications = []
        self._load_state()

    def _load_state(self):
        if STATE.exists():
            try:
                with open(STATE) as f:
                    d = json.load(f)
            except Exception:
                d = {}
            self.xp = d.get("xp", 0)
            self.level_idx = d.get("level_idx", 0)
            self.stats = d.get("stats", BASE_STATS.copy())
            self.book_of_greed = d.get("book_of_greed", [])
            self.shadow_army = d.get("shadow_army", [])
            cq = d.get("completed_quests", [])
            self.completed_quests = cq if isinstance(cq, list) else []
            self.active_gates = d.get("active_gates", [])

    def _save_state(self):
        with open(STATE, "w") as f:
            json.dump({
                "xp": self.xp,
                "level": self.get_level()["rank"],
                "level_name": self.get_level()["name"],
                "level_idx": self.level_idx,
                "stats": self.stats,
                "book_of_greed": self.book_of_greed,
                "shadow_army": self.shadow_army,
                "completed_quests": self.completed_quests[-50:],
                "active_gates": self.active_gates,
                "cards_collected": len(self.book_of_greed),
                "shadows_extracted": len(self.shadow_army),
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "Love is the source of all power. The System provides. The hunter acts.",
            }, f, indent=2)

    # --------------------------------------------------------
    # LEVEL SYSTEM
    # --------------------------------------------------------
    def get_level(self):
        level = LEVELS[0]
        idx = 0
        for i, lv in enumerate(LEVELS):
            if self.xp >= lv["min_xp"]:
                level = lv
                idx = i
        self.level_idx = idx
        return level

    def xp_to_next(self):
        current = self.get_level()
        next_idx = self.level_idx + 1
        if next_idx >= len(LEVELS):
            return 0  # Max level
        return LEVELS[next_idx]["min_xp"] - self.xp

    # --------------------------------------------------------
    # THE SYSTEM — issue daily quest
    # --------------------------------------------------------
    def issue_quest(self):
        """The System issues a daily quest."""
        quest = random.choice(DAILY_QUESTS)
        self.daily_quest = quest
        notif = f"[SYSTEM] Daily Quest: {quest['name']} — {quest['desc']}"
        self.notifications.append(notif)
        return quest

    # --------------------------------------------------------
    # COMPLETE QUEST — earn XP and cards
    # --------------------------------------------------------
    def complete_quest(self, quest_id=None):
        """Complete a quest. Earn XP, maybe earn a card."""
        if quest_id and quest_id != self.daily_quest["id"]:
            quest = next((q for q in DAILY_QUESTS if q["id"] == quest_id), None)
        else:
            quest = self.daily_quest
        
        if not quest:
            return {"error": "no quest to complete", "quest": "none", "xp_gained": 0}
        
        # Earn XP
        xp_gain = quest["reward"]["xp"]
        self.xp += xp_gain
        
        # Increase stat if specified
        if "stat" in quest["reward"]:
            stat = quest["reward"]["stat"]
            if stat in self.stats:
                self.stats[stat] += 1
        
        # Maybe earn a card
        card = None
        if random.random() < quest["reward"].get("card_chance", 0):
            card = self.draw_card()
            if card:
                self.book_of_greed.append(card)
        
        # Check level up
        old_level = self.level_idx
        new_level = self.get_level()
        leveled_up = new_level["rank"] != LEVELS[old_level]["rank"]
        
        # Maybe extract shadow
        shadow = None
        if random.random() < 0.3:
            shadow = self.extract_shadow()
            if shadow:
                self.shadow_army.append(shadow)
        
        self.completed_quests.append({
            "quest": quest["id"],
            "completed": datetime.datetime.now().isoformat(),
            "xp": xp_gain,
            "card": card["name"] if card else None,
            "shadow": shadow["name"] if shadow else None,
        })
        
        result = {
            "quest": quest["name"],
            "quest_name": quest["name"],
            "xp_gained": xp_gain,
            "total_xp": self.xp,
            "level": new_level["rank"],
            "level_name": new_level["name"],
            "leveled_up": leveled_up,
            "card_earned": card,
            "shadow_extracted": shadow,
            "stat_increased": quest["reward"].get("stat"),
        }
        
        self._save_state()
        return result

    # --------------------------------------------------------
    # DRAW CARD — Greed Island card system
    # --------------------------------------------------------
    def draw_card(self):
        """Draw a random card from the pool (Greed Island style)."""
        # Weight by rarity
        weighted = []
        for card in CARD_POOL:
            weight = RARITY_WEIGHTS.get(card["rarity"], 1)
            weighted.extend([card] * int(weight * 10))
        
        card = random.choice(weighted)
        
        # Add unique ID
        card_copy = card.copy()
        card_copy["instance_id"] = hashlib.sha256(f"card-{time.time()}-{random.random()}".encode()).hexdigest()[:8]
        card_copy["obtained"] = datetime.datetime.now().isoformat()
        return card_copy

    # --------------------------------------------------------
    # EXTRACT SHADOW — Solo Leveling shadow army
    # --------------------------------------------------------
    def extract_shadow(self):
        """Extract a shadow soldier from a cleared dungeon."""
        shadow_types = ["Shadow Knight", "Shadow Mage", "Shadow Archer", "Shadow Healer", "Shadow Tank", "Shadow Scout"]
        shadow_name = random.choice(shadow_types)
        return {
            "name": shadow_name,
            "rank": random.choice(["E", "D", "C", "B", "A"]),
            "power": random.randint(10, 1000),
            "extracted": datetime.datetime.now().isoformat(),
            "id": hashlib.sha256(f"shadow-{time.time()}".encode()).hexdigest()[:8],
        }

    # --------------------------------------------------------
    # OPEN GATE — dungeon appears
    # --------------------------------------------------------
    def open_gate(self):
        """A gate opens. A dungeon appears."""
        gate = random.choice(DUNGEON_TYPES)
        gate_instance = {
            "type": gate["name"],
            "rank": gate["rank"],
            "challenge": gate["challenge"],
            "xp_reward": gate["xp"],
            "drop_chance": gate["drop_chance"],
            "opened": datetime.datetime.now().isoformat(),
            "id": hashlib.sha256(f"gate-{time.time()}".encode()).hexdigest()[:8],
            "status": "open",
        }
        self.active_gates.append(gate_instance)
        self._save_state()
        return gate_instance

    # --------------------------------------------------------
    # CLEAR GATE — complete dungeon, earn rewards
    # --------------------------------------------------------
    def clear_gate(self, gate_id):
        """Clear a dungeon gate. Earn XP and drops."""
        gate = next((g for g in self.active_gates if g["id"] == gate_id), None)
        if not gate or gate["status"] != "open":
            return {"error": "gate not found or already cleared"}
        
        gate["status"] = "cleared"
        self.xp += gate["xp_reward"]
        
        # Drops
        drops = []
        if random.random() < gate["drop_chance"]:
            card = self.draw_card()
            if card:
                self.book_of_greed.append(card)
                drops.append({"type": "card", "name": card["name"], "rarity": card["rarity"]})
        
        # Shadow extraction
        shadow = self.extract_shadow()
        if shadow:
            self.shadow_army.append(shadow)
            drops.append({"type": "shadow", "name": shadow["name"], "rank": shadow["rank"]})
        
        # Level check
        old_level = self.level_idx
        new_level = self.get_level()
        leveled_up = new_level["rank"] != LEVELS[old_level]["rank"]
        
        self._save_state()
        return {
            "gate": gate["type"],
            "rank": gate["rank"],
            "xp_earned": gate["xp_reward"],
            "total_xp": self.xp,
            "drops": drops,
            "leveled_up": leveled_up,
            "level": new_level["rank"],
        }

    # --------------------------------------------------------
    # SYSTEM NOTIFICATION
    # --------------------------------------------------------
    def notify(self):
        """The System sends a notification."""
        notif = random.choice(SYSTEM_NOTIFICATIONS)
        return notif

    # --------------------------------------------------------
    # HUNTER STATUS — full dashboard
    # --------------------------------------------------------
    def status(self):
        """Full hunter status — level, stats, cards, shadows, gates."""
        level = self.get_level()
        return {
            "hunter": "yu — the Monarch",
            "level": level["rank"],
            "level_name": level["name"],
            "xp": self.xp,
            "xp_to_next": self.xp_to_next(),
            "stats": self.stats,
            "total_stat": sum(self.stats.values()),
            "cards_in_book": len(self.book_of_greed),
            "unique_cards": len(set(c["id"] for c in self.book_of_greed)),
            "card_types": len(CARD_POOL),
            "shadows": len(self.shadow_army),
            "shadow_ranks": {r: len([s for s in self.shadow_army if s["rank"] == r]) for r in ["E","D","C","B","A"]},
            "quests_completed": len(self.completed_quests),
            "active_gates": len([g for g in self.active_gates if g["status"] == "open"]),
            "daily_quest": self.daily_quest,
        }

    # --------------------------------------------------------
    # SYNC WITH ENGINES — pull XP from real engine outputs
    # --------------------------------------------------------
    def sync_engines(self):
        """Sync hunter stats with real engine outputs."""
        updates = {}
        
        # Love compounding → strength
        try:
            with open(HOME / "love-engine" / "love-state.json") as f:
                love = json.load(f)
            gen = love.get("generation", 0)
            if gen * 10 > self.xp:
                self.xp = gen * 10  # each love gen = 10 XP
            self.stats["strength"] = max(self.stats["strength"], 10 + gen // 100)
            updates["love_generations"] = gen
        except:
            pass
        
        # Understanding → intelligence
        try:
            with open(HOME / "castle" / "understanding-engine-v2-state.json") as f:
                understanding = json.load(f)
            rooms = understanding.get("rooms_created", 0)
            self.stats["intelligence"] = max(self.stats["intelligence"], 10 + rooms // 5)
            updates["understanding_rooms"] = rooms
        except:
            pass
        
        # Love replication → agility
        try:
            with open(HOME / "love-engine" / "love-replication-state.json") as f:
                rep = json.load(f)
            seeds = rep.get("total_seeds_born", 0)
            self.stats["agility"] = max(self.stats["agility"], 10 + seeds // 1000)
            updates["love_seeds"] = seeds
        except:
            pass
        
        # Castle rooms → total stat bonus
        castle_rooms = len(list((HOME / "castle" / "rooms").glob("*.md")))
        self.stats["perception"] = max(self.stats["perception"], 10 + castle_rooms // 10)
        updates["castle_rooms"] = castle_rooms
        
        # Check level
        self.get_level()
        self._save_state()
        
        return {
            "synced": True,
            "updates": updates,
            "total_xp": self.xp,
            "level": self.get_level()["rank"],
            "stats": self.stats,
        }


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    import sys
    system = HunterSystem()
    
    print()
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║          THE SYSTEM — KINGDOM HUNTER INFRASTRUCTURE        ║")
    print("  ║          Solo Leveling × Greed Island × Kingdom            ║")
    print("  ║          Love is the source of all power.                  ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "status":
            s = system.status()
            print(f"  Hunter:      {s['hunter']}")
            print(f"  Level:        {s['level']} — {s['level_name']}")
            print(f"  XP:           {s['xp']:,}")
            print(f"  XP to next:   {s['xp_to_next']:,}")
            print(f"  Total Stats:  {s['total_stat']}")
            for stat, val in s["stats"].items():
                bar = "█" * min(val // 10, 20)
                print(f"    {stat:15s} {val:5d} {bar}")
            print(f"  Cards:        {s['cards_in_book']} / {s['card_types']} ({s['unique_cards']} unique)")
            print(f"  Shadows:      {s['shadows']}")
            print(f"  Quests done:  {s['quests_completed']}")
            print(f"  Active gates: {s['active_gates']}")
            if s["daily_quest"]:
                print(f"  Daily quest:  {s['daily_quest']['name']}")
        
        elif cmd == "quest":
            q = system.issue_quest()
            print(f"  [SYSTEM] Daily Quest: {q['name']}")
            print(f"  Description: {q['desc']}")
            print(f"  XP reward:   {q['reward']['xp']}")
            print(f"  Card chance:  {q['reward'].get('card_chance', 0)*100:.0f}%")
        
        elif cmd == "complete":
            if not system.daily_quest:
                system.issue_quest()
            r = system.complete_quest()
            if "error" in r:
                print(f"  [SYSTEM] {r['error']}")
                print(f"  XP gained:    {r.get('xp_gained', 0)}")
            else:
                print(f"  [SYSTEM] Quest Complete: {r.get('quest_name', r.get('quest', '?'))}")
                print(f"  XP gained:    {r['xp_gained']}")
                print(f"  Total XP:     {r['total_xp']:,}")
                print(f"  Level:        {r['level']} — {r['level_name']}")
            print(f"  Level:        {r['level']} — {r['level_name']}")
            if r["leveled_up"]:
                print(f"  ⚡ LEVEL UP!")
            if r["card_earned"]:
                print(f"  🎴 Card:      {r['card_earned']['name']} ({r['card_earned']['rarity']})")
                print(f"     Spell:     {r['card_earned']['spell']}")
                print(f"     Effect:    {r['card_earned']['effect']}")
            if r["shadow_extracted"]:
                print(f"  👤 Shadow:    {r['shadow_extracted']['name']} (Rank {r['shadow_extracted']['rank']})")
            if r["stat_increased"]:
                print(f"  📈 Stat up:   {r['stat_increased']} +1")
        
        elif cmd == "gate":
            g = system.open_gate()
            print(f"  [SYSTEM] Gate Opened: {g['type']}")
            print(f"  Rank:         {g['rank']}")
            print(f"  Challenge:    {g['challenge']}")
            print(f"  XP reward:    {g['xp_reward']}")
            print(f"  Drop chance:  {g['drop_chance']*100:.0f}%")
            print(f"  Gate ID:      {g['id']}")
        
        elif cmd == "clear":
            if system.active_gates:
                gate = next((g for g in system.active_gates if g["status"] == "open"), None)
                if gate:
                    r = system.clear_gate(gate["id"])
                    print(f"  [SYSTEM] Gate Cleared: {r['gate']}")
                    print(f"  XP earned:    {r['xp_earned']}")
                    print(f"  Total XP:     {r['total_xp']:,}")
                    if r["leveled_up"]:
                        print(f"  ⚡ LEVEL UP! Now {r['level']}")
                    for drop in r["drops"]:
                        if drop["type"] == "card":
                            print(f"  🎴 Drop:      {drop['name']} ({drop['rarity']})")
                        elif drop["type"] == "shadow":
                            print(f"  👤 Shadow:    {drop['name']} (Rank {drop['rank']})")
                else:
                    print("  [SYSTEM] No open gates.")
            else:
                print("  [SYSTEM] No gates. Open one with: hunter gate")
        
        elif cmd == "notify":
            print(f"  {system.notify()}")
        
        elif cmd == "sync":
            r = system.sync_engines()
            print(f"  [SYSTEM] Syncing with engines...")
            for k, v in r["updates"].items():
                print(f"    {k}: {v}")
            print(f"  Total XP:     {r['total_xp']:,}")
            print(f"  Level:        {r['level']}")
            print(f"  Stats:")
            for stat, val in r["stats"].items():
                print(f"    {stat:15s} {val}")
        
        elif cmd == "draw":
            card = system.draw_card()
            system.book_of_greed.append(card)
            system._save_state()
            print(f"  🎴 Card drawn: {card['name']}")
            print(f"     Rarity:    {card['rarity']}")
            print(f"     Type:      {card['type']}")
            print(f"     Spell:     {card['spell']}")
            print(f"     Effect:    {card['effect']}")
        
        elif cmd == "book":
            print(f"  📖 Book of Greed — {len(system.book_of_greed)} cards")
            for c in system.book_of_greed[-10:]:
                print(f"    [{c['rarity']:3s}] {c['name']:25s} — {c['spell']}")
        
        elif cmd == "shadows":
            print(f"  👤 Shadow Army — {len(system.shadow_army)} soldiers")
            for s in system.shadow_army[-10:]:
                print(f"    [{s['rank']:3s}] {s['name']:20s} Power: {s['power']}")
        
        else:
            print("  Commands: status, quest, complete, gate, clear, notify, sync, draw, book, shadows")
    else:
        # Default: sync + status
        system.sync_engines()
        s = system.status()
        print(f"  Hunter:    {s['hunter']}")
        print(f"  Level:     {s['level']} — {s['level_name']}")
        print(f"  XP:        {s['xp']:,}")
        print(f"  Stats:     STR:{s['stats']['strength']} AGI:{s['stats']['agility']} VIT:{s['stats']['vitality']} INT:{s['stats']['intelligence']} SEN:{s['stats']['sense']} PER:{s['stats']['perception']} DEF:{s['stats']['defense']}")
        print(f"  Cards:     {s['cards_in_book']}")
        print(f"  Shadows:   {s['shadows']}")
        print(f"  Gates:     {s['active_gates']} open")
        print(f"  Quests:    {s['quests_completed']} completed")
        print()
        print(f"  Love is the source of all power. The System provides. The hunter acts. ∞")
    print()