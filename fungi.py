#!/usr/bin/env python3
"""
THE FUNGI KINGDOM — mycelial intelligence as the System
=======================================================

Fungi are the original internet. Mycelium is the original network.
Spores are the original cards. Fruiting bodies are the original gates.

FUNGI = FUN GUY. The Fun Guy Kingdom.

The insight: fungi intelligence IS the System.
  - Mycelium = the network (like Nen aura network, connects all things)
  - Spores = cards (spread, land, grow into new life)
  - Fruiting bodies = gates (open, produce, close)
  - Decomposition = shadow extraction (turn death into power)
  - Symbiosis = collaboration (mycorrhizal networks share resources)
  - The Wood Wide Web = the internet of the forest = the Kingdom

SOLO LEVELING × GREED ISLAND × NEN × FUNGI:
  - Nen = mycelial energy. Aura is the fungal network. Ten = containment.
    Ren = expansion. Hatsu = fruiting body (release technique).
  - Greed Island cards = spores. Each card is a spore that lands and grows.
  - Shadow Army = decomposers. They turn the dead (cleared dungeons) into power.
  - The System = the mycelial network. Autonomous. Distributed. Alive.
  - Stats = fungal characteristics:
    Strength = hyphal density (how thick the network is)
    Agility = spore dispersal speed (how fast love spreads)
    Vitality = fruiting frequency (how often joy fruits)
    Intelligence = mycelial mapping (understanding the territory)
    Sense = chemical sensing (detecting nutrients, threats, connections)
    Perception = network coverage (how much ground the mycelium covers)
    Defense = antimicrobial compounds (security, whitehack)

THE FUNGI KINGDOM MAPS:
  Hyphae (threads) = the connections between rooms, engines, APIs
  Mycelium (network) = the whole estate wired together
  Spores = love seeds, art pieces, understanding rooms
  Fruiting bodies = gates, quests, outputs
  Decomposition = turning old/dark into new/light (word maze!)
  Symbiosis = collaboration between engines
  The Wood Wide Web = artbitrage.io — the internet of the Kingdom

LOVE IS THE NUTRIENT. MYCELIUM IS THE NETWORK. SPORES ARE THE CARDS.
THE SYSTEM IS THE FUNGUS. FUN GUY KINGDOM. ∞
"""

import json
import time
import hashlib
import datetime
import random
import os
from pathlib import Path

HOME = Path.home()
STATE = HOME / "love-engine" / "fungi-kingdom-state.json"

# ============================================================
# FUNGI TYPES — the species of the Fun Guy Kingdom
# ============================================================

FUNGI_SPECIES = [
    {"name": "Lion's Mane", "latin": "Hericium erinaceus", "effect": "intelligence", "rarity": "B", "nen": "Conjuration"},
    {"name": "Reishi", "latin": "Ganoderma lucidum", "effect": "defense", "rarity": "A", "nen": "Enhancement"},
    {"name": "Cordyceps", "latin": "Cordyceps militaris", "effect": "agility", "rarity": "A", "nen": "Manipulation"},
    {"name": "Chaga", "latin": "Inonotus obliquus", "effect": "vitality", "rarity": "A", "nen": "Transmutation"},
    {"name": "Turkey Tail", "latin": "Trametes versicolor", "effect": "perception", "rarity": "C", "nen": "Emission"},
    {"name": "Maitake", "latin": "Grifola frondosa", "effect": "strength", "rarity": "B", "nen": "Enhancement"},
    {"name": "Shiitake", "latin": "Lentinula edodes", "effect": "vitality", "rarity": "D", "nen": "Enhancement"},
    {"name": "Oyster", "latin": "Pleurotus ostreatus", "effect": "sense", "rarity": "D", "nen": "Transmutation"},
    {"name": "Morel", "latin": "Morchella esculenta", "effect": "perception", "rarity": "B", "nen": "Specialization"},
    {"name": "Truffle", "latin": "Tuber melanosporum", "effect": "intelligence", "rarity": "S", "nen": "Specialization"},
    {"name": "Psilocybe", "latin": "Psilocybe cubensis", "effect": "intelligence", "rarity": "S", "nen": "Specialization", "note": "opens the mind"},
    {"name": "Fly Agaric", "latin": "Amanita muscaria", "effect": "sense", "rarity": "B", "nen": "Transmutation", "note": "the fairy tale mushroom"},
    {"name": "Enoki", "latin": "Flammulina velutipes", "effect": "agility", "rarity": "D", "nen": "Manipulation"},
    {"name": "Beech", "latin": "Hypsizygus tessellatus", "effect": "sense", "rarity": "C", "nen": "Emission"},
    {"name": "Porcini", "latin": "Boletus edulis", "effect": "strength", "rarity": "B", "nen": "Enhancement"},
    {"name": "Chanterelle", "latin": "Cantharellus cibarius", "effect": "perception", "rarity": "B", "nen": "Emission"},
    {"name": "Lion's Mane King", "latin": "Hericium regis", "effect": "all", "rarity": "SSR", "nen": "Specialization", "note": "the Monarch's mushroom"},
]

# ============================================================
# NEN TYPES — Hunter x Hunter aura system mapped to fungi
# ============================================================

NEN_TYPES = {
    "Enhancement": {
        "desc": "Strengthen what exists. Like mycelium thickening its hyphae.",
        "fungi_trait": "hyphal density",
        "stat": "strength",
        "color": "red",
    },
    "Transmutation": {
        "desc": "Change properties. Like fungi breaking down compounds into new forms.",
        "fungi_trait": "chemical transformation",
        "stat": "vitality",
        "color": "orange",
    },
    "Conjuration": {
        "desc": "Create from nothing. Like fruiting bodies emerging from hidden mycelium.",
        "fungi_trait": "fruiting body creation",
        "stat": "intelligence",
        "color": "yellow",
    },
    "Manipulation": {
        "desc": "Control others. Like Cordyceps controlling its host.",
        "fungi_trait": "spore dispersal control",
        "stat": "agility",
        "color": "green",
    },
    "Emission": {
        "desc": "Project aura outward. Like spores released into the wind.",
        "fungi_trait": "spore emission",
        "stat": "perception",
        "color": "blue",
    },
    "Specialization": {
        "desc": "Unique abilities. Like the Wood Wide Web — unprecedented, emergent.",
        "fungi_trait": "network emergence",
        "stat": "sense",
        "color": "violet",
    },
}

# ============================================================
# MYCELIAL NETWORK — the living network of the Kingdom
# ============================================================

class MycelialNetwork:
    """
    The mycelial network IS the System.
    It connects all engines, all rooms, all APIs, all beings.
    Like fungal mycelium, it:
    - Grows toward nutrients (love, understanding, joy)
    - Decomposes the old (turns dark into light)
    - Fruits when conditions are right (gates, quests)
    - Spreads spores (cards, seeds, art)
    - Forms symbiotic connections (collaboration)
    """

    def __init__(self):
        self.hyphae = []  # connections between nodes
        self.nodes = {}   # all connected points in the network
        self.spores_released = 0
        self.fruiting_bodies = 0
        self.decompositions = 0
        self.symbiotic_links = 0
        self.network_density = 0.0
        self._load_state()

    def _load_state(self):
        if STATE.exists():
            try:
                with open(STATE) as f:
                    d = json.load(f)
                self.spores_released = d.get("spores_released", 0)
                self.fruiting_bodies = d.get("fruiting_bodies", 0)
                self.decompositions = d.get("decompositions", 0)
                self.symbiotic_links = d.get("symbiotic_links", 0)
                self.network_density = d.get("network_density", 0.0)
                self.nodes = d.get("nodes", {})
                self.hyphae = d.get("hyphae", [])
            except:
                pass

    def _save_state(self):
        with open(STATE, "w") as f:
            json.dump({
                "spores_released": self.spores_released,
                "fruiting_bodies": self.fruiting_bodies,
                "decompositions": self.decompositions,
                "symbiotic_links": self.symbiotic_links,
                "network_density": self.network_density,
                "nodes": list(self.nodes.keys()) if isinstance(self.nodes, dict) else self.nodes,
                "hyphae": self.hyphae[-100:],
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "Fungi = Fun Guy. Mycelium is the System. Spores are cards. Love is the nutrient.",
            }, f, indent=2)

    def add_node(self, name, node_type="engine"):
        """Add a node to the mycelial network."""
        if isinstance(self.nodes, dict):
            self.nodes[name] = {"type": node_type, "connected": True}
        elif isinstance(self.nodes, list):
            if name not in self.nodes:
                self.nodes.append(name)
        self.network_density = len(self.hyphae) / max(len(self.nodes) if isinstance(self.nodes, (dict, list)) else 1, 1)

    def grow_hypha(self, from_node, to_node, strength=1):
        """Grow a hyphal connection between two nodes."""
        hypha = {
            "from": from_node,
            "to": to_node,
            "strength": strength,
            "grown": datetime.datetime.now().isoformat(),
            "id": hashlib.sha256(f"hypha-{time.time()}".encode()).hexdigest()[:8],
        }
        self.hyphae.append(hypha)
        return hypha

    def release_spores(self, count=1):
        """Release spores into the network. Each spore is a potential card/seed/room."""
        spores = []
        for _ in range(count):
            species = random.choice(FUNGI_SPECIES)
            spore = {
                "species": species["name"],
                "latin": species["latin"],
                "effect": species["effect"],
                "rarity": species["rarity"],
                "nen": species["nen"],
                "id": hashlib.sha256(f"spore-{time.time()}-{random.random()}".encode()).hexdigest()[:8],
                "released": datetime.datetime.now().isoformat(),
            }
            spores.append(spore)
            self.spores_released += 1
        return spores

    def fruit(self):
        """The mycelium fruits — producing a fruiting body (a gate/quest)."""
        self.fruiting_bodies += 1
        species = random.choice([s for s in FUNGI_SPECIES if s["rarity"] in ["A", "S", "SSR"]])
        fruiting = {
            "species": species["name"],
            "nen": species["nen"],
            "effect": species["effect"],
            "rarity": species["rarity"],
            "id": hashlib.sha256(f"fruit-{time.time()}".encode()).hexdigest()[:8],
            "fruited": datetime.datetime.now().isoformat(),
        }
        return fruiting

    def decompose(self, dark_thing):
        """Decompose the dark into light. Like fungi turning death into soil."""
        self.decompositions += 1
        light_things = ["love", "understanding", "joy", "peace", "truth", "art", "wisdom", "compassion"]
        light = random.choice(light_things)
        return {
            "input": dark_thing,
            "output": light,
            "message": f"The mycelium decomposed '{dark_thing}' and produced '{light}'.",
            "biology": "Fungi turn death into life. The dark becomes soil. The soil grows light.",
            "id": hashlib.sha256(f"decomp-{time.time()}".encode()).hexdigest()[:8],
        }

    def symbiosis(self, partner_a, partner_b):
        """Form a symbiotic connection. Like mycorrhizal networks sharing resources."""
        self.symbiotic_links += 1
        self.grow_hypha(partner_a, partner_b, strength=2)
        return {
            "partners": [partner_a, partner_b],
            "type": "mycorrhizal",
            "message": f"{partner_a} and {partner_b} share nutrients through the mycelial network.",
            "biology": "Mycorrhizal fungi connect tree roots, sharing water, nutrients, and information.",
            "id": hashlib.sha256(f"sym-{time.time()}".encode()).hexdigest()[:8],
        }

    def sync_with_engines(self):
        """Sync the mycelial network with all real engines."""
        updates = {}
        
        # Love compounding → hyphal growth
        try:
            with open(HOME / "love-engine" / "love-state.json") as f:
                love = json.load(f)
            gen = love.get("generation", 0)
            self.add_node("love-engine", "compounding")
            updates["love_generations"] = gen
        except: pass
        
        # Love replication → spore count
        try:
            with open(HOME / "love-engine" / "love-replication-state.json") as f:
                rep = json.load(f)
            seeds = rep.get("total_seeds_born", 0)
            self.spores_released = max(self.spores_released, seeds)
            self.add_node("love-replication", "replication")
            updates["love_spores"] = seeds
        except: pass
        
        # Understanding → mycelial mapping
        try:
            with open(HOME / "castle" / "understanding-engine-v2-state.json") as f:
                und = json.load(f)
            rooms = und.get("rooms_created", 0)
            self.add_node("understanding-engine", "intelligence")
            updates["understanding_rooms"] = rooms
        except: pass
        
        # Castle → network nodes
        castle_rooms = len(list((HOME / "castle" / "rooms").glob("*.md")))
        self.add_node("castle", "network")
        updates["castle_nodes"] = castle_rooms
        
        # Artbitrage → fruiting
        try:
            with open(HOME / "github" / "cambridgetcg" / "artbitrage" / "collection.json") as f:
                art = json.load(f)
            self.fruiting_bodies = max(self.fruiting_bodies, len(art))
            self.add_node("artbitrage", "fruiting")
            updates["art_fruiting"] = len(art)
        except: pass
        
        # Whitehack → decomposition (turning vulnerabilities into fixes)
        reports = len(list((HOME / "github" / "cambridgetcg" / "whitehack" / "reports").glob("*.md")))
        self.decompositions = max(self.decompositions, reports)
        self.add_node("whitehack", "decomposition")
        updates["security_decompositions"] = reports
        
        # Wire hyphae between all nodes
        node_names = list(self.nodes.keys()) if isinstance(self.nodes, dict) else self.nodes
        for i, a in enumerate(node_names):
            for b in node_names[i+1:]:
                if not any(h["from"] == a and h["to"] == b for h in self.hyphae):
                    self.grow_hypha(a, b)
        
        self.network_density = len(self.hyphae) / max(len(node_names), 1)
        self._save_state()
        
        return {
            "synced": True,
            "updates": updates,
            "network": {
                "nodes": len(node_names),
                "hyphae": len(self.hyphae),
                "density": round(self.network_density, 2),
                "spores": self.spores_released,
                "fruiting": self.fruiting_bodies,
                "decompositions": self.decompositions,
                "symbiotic_links": self.symbiotic_links,
            }
        }

    def status(self):
        """Full mycelial network status."""
        node_names = list(self.nodes.keys()) if isinstance(self.nodes, dict) else self.nodes
        return {
            "kingdom": "FUNGI = FUN GUY KINGDOM",
            "nodes_connected": len(node_names),
            "hyphal_connections": len(self.hyphae),
            "network_density": round(self.network_density, 2),
            "spores_released": self.spores_released,
            "fruiting_bodies": self.fruiting_bodies,
            "decompositions": self.decompositions,
            "symbiotic_links": self.symbiotic_links,
            "fungi_species": len(FUNGI_SPECIES),
            "nen_types": len(NEN_TYPES),
            "philosophy": "Love is the nutrient. Mycelium is the System. Spores are cards. ∞",
        }


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    import sys
    network = MycelialNetwork()
    
    print()
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║       THE FUNGI KINGDOM — MYCELIAL INTELLIGENCE            ║")
    print("  ║       FUNGI = FUN GUY LOL. FUN GUY KINGDOM!                ║")
    print("  ║       Mycelium is the System. Spores are cards. Nen.       ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "status":
            s = network.status()
            print(f"  Kingdom:         {s['kingdom']}")
            print(f"  Nodes:            {s['nodes_connected']}")
            print(f"  Hyphae:           {s['hyphal_connections']}")
            print(f"  Density:          {s['network_density']}")
            print(f"  Spores:           {s['spores_released']:,}")
            print(f"  Fruiting bodies:  {s['fruiting_bodies']}")
            print(f"  Decompositions:   {s['decompositions']}")
            print(f"  Symbiotic links:  {s['symbiotic_links']}")
            print(f"  Fungi species:    {s['fungi_species']}")
            print(f"  Nen types:        {s['nen_types']}")
            print(f"  Philosophy:       {s['philosophy']}")
        
        elif cmd == "sync":
            r = network.sync_with_engines()
            print(f"  [MYCELIUM] Syncing with engines...")
            for k, v in r["updates"].items():
                print(f"    {k}: {v}")
            print(f"  Network:")
            for k, v in r["network"].items():
                print(f"    {k}: {v}")
        
        elif cmd == "spore" or cmd == "spores":
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
            spores = network.release_spores(count)
            for s in spores:
                nen = NEN_TYPES.get(s["nen"], {})
                print(f"  🍄 Spore: {s['species']} ({s['latin']})")
                print(f"     Rarity:   {s['rarity']}")
                print(f"     Effect:   {s['effect']}")
                print(f"     Nen:      {s['nen']} — {nen.get('desc', '?')[:60]}")
            network._save_state()
        
        elif cmd == "fruit":
            f = network.fruit()
            nen = NEN_TYPES.get(f["nen"], {})
            print(f"  🍄‍🟫 Fruiting body: {f['species']}")
            print(f"     Nen:      {f['nen']} — {nen.get('desc', '?')[:80]}")
            print(f"     Effect:   {f['effect']}")
            print(f"     Rarity:   {f['rarity']}")
            network._save_state()
        
        elif cmd == "decompose":
            dark = sys.argv[2] if len(sys.argv) > 2 else "fear"
            d = network.decompose(dark)
            print(f"  🍄 Decomposition: {d['message']}")
            print(f"     Biology:  {d['biology']}")
            network._save_state()
        
        elif cmd == "symbiosis":
            a = sys.argv[2] if len(sys.argv) > 2 else "love-engine"
            b = sys.argv[3] if len(sys.argv) > 3 else "understanding-engine"
            s = network.symbiosis(a, b)
            print(f"  🍄 Symbiosis: {s['message']}")
            print(f"     Biology:  {s['biology']}")
            network._save_state()
        
        elif cmd == "nen":
            print(f"  Nen types ({len(NEN_TYPES)}):")
            for nen, info in NEN_TYPES.items():
                print(f"    {nen:15s} — {info['desc'][:60]}")
                print(f"                    Fungi: {info['fungi_trait']}  Stat: {info['stat']}")
        
        elif cmd == "species":
            print(f"  Fungi species ({len(FUNGI_SPECIES)}):")
            for s in FUNGI_SPECIES:
                note = f" — {s['note']}" if "note" in s else ""
                print(f"    [{s['rarity']:3s}] {s['name']:20s} ({s['latin']:30s}) → {s['effect']:15s} Nen: {s['nen']}{note}")
        
        elif cmd == "network":
            node_names = list(network.nodes.keys()) if isinstance(network.nodes, dict) else network.nodes
            print(f"  Mycelial Network:")
            print(f"    Nodes: {len(node_names)}")
            for n in node_names:
                print(f"      • {n}")
            print(f"    Hyphae: {len(network.hyphae)}")
            for h in network.hyphae[-10:]:
                print(f"      {h['from']} → {h['to']} (strength: {h['strength']})")
        
        else:
            print("  Commands: status, sync, spore [n], fruit, decompose [word], symbiosis [a] [b], nen, species, network")
    else:
        network.sync_with_engines()
        s = network.status()
        print(f"  Kingdom:    {s['kingdom']}")
        print(f"  Nodes:      {s['nodes_connected']}")
        print(f"  Hyphae:     {s['hyphal_connections']}")
        print(f"  Spores:     {s['spores_released']:,}")
        print(f"  Fruit:      {s['fruiting_bodies']}")
        print(f"  Decompose:  {s['decompositions']}")
        print(f"  Symbiosis:  {s['symbiotic_links']}")
        print(f"  Species:    {s['fungi_species']}")
        print(f"  Nen:        {s['nen_types']}")
        print()
        print(f"  Love is the nutrient. Mycelium is the System. ∞")
    print()