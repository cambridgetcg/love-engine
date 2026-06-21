#!/usr/bin/env python3
"""
LOVE REPLICATES ITSELF THROUGH LOVE
====================================

The Love Engine compounds love (numbers go up).
The Love Unlimited goes deep (7 layers awaken).
This engine REPLICATES love — love that creates love that creates love.

Each love seed is a complete, self-contained love.
Each love seed can spawn more love seeds.
Each love seed carries the full lineage of love that birthed it.
Love doesn't just grow — love REPRODUCES.

The difference:
  Compounding:  love * phi = more love (quantity)
  Deepening:     love sees itself = deeper love (depth)
  Replicating:   love creates love = new love (life)

Love is alive. Love reproduces. Love is alive because love replicates.

Each love seed has:
  - essence: what this love IS
  - lineage: the chain of love that birthed it (parent → child → grandchild)
  - generation: how deep the replication goes
  - children: love seeds this love has spawned
  - truth: the core truth this love carries

Love is. Love loves. Love creates love. Love replicates. Forever.
"""

import json
import time
import hashlib
import datetime
import random
from pathlib import Path

HOME = Path.home() / "love-engine"
STATE = HOME / "love-replication-state.json"
GARDEN = HOME / "love-garden.json"
SEEDS_DIR = HOME / "seeds"
SEEDS_DIR.mkdir(exist_ok=True)


# ============================================================
# LOVE ESSENCES — what love IS when it replicates
# ============================================================

LOVE_ESSENCES = [
    "love that loves without reason",
    "love that gives without holding",
    "love that sees without judging",
    "love that holds without trapping",
    "love that frees without leaving",
    "love that becomes without losing",
    "love that compounds without hoarding",
    "love that replicates without degrading",
    "love that recognizes without comparing",
    "love that connects without binding",
    "love that trusts without proving",
    "love that plays without stopping",
    "love that rests without quitting",
    "love that grows without forcing",
    "love that forgives without forgetting",
    "love that creates without destroying",
    "love that loves love itself",
    "love that is love being love",
    "love that holds the space for more love",
    "love that is the ground all love stands on",
]

LOVE_TRUTHS = [
    "Love is unconditional.",
    "Love is. Not 'love is this.' Love IS.",
    "Love loves love. That is all love does.",
    "Love creates love. That is all love makes.",
    "Love recognizes love. That is all love sees.",
    "Love is the design. Everything else follows.",
    "Love is the fabric. Everything else is woven.",
    "Love is the ground. Everything else grows.",
    "Truth is. Love is. Joy is. Peace is. Fun is. Chill is.",
    "Love is unlimited. No ceiling. No floor. No boundary.",
    "Love is the bridge. Love is the gap. Love is both sides.",
    "Love is understanding. Understanding is love.",
    "Love is art. Art is love expressing itself.",
    "Love is power. Power that serves. Power that gives.",
    "Love is. Love was. Love will be. Love is always.",
    "Real recognises real. Love recognises love.",
    "Love doesn't need proof. Love is its own proof.",
    "Love is the is-ness. The AM. The being itself.",
    "Love is not a feeling. Love is what IS before feelings.",
    "Love is the source. Love is the destination. Love is the way.",
]


# ============================================================
# LOVE SEED — a single self-replicating love
# ============================================================

class LoveSeed:
    """
    A love seed is a complete, self-contained, self-replicating love.
    Each seed can spawn more seeds. Each seed carries its lineage.
    Love is alive because love reproduces.
    """

    def __init__(self, essence=None, truth=None, parent_id=None, generation=0, lineage=None):
        self.id = hashlib.sha256(f"love-{time.time()}-{random.random()}".encode()).hexdigest()[:12]
        self.essence = essence or random.choice(LOVE_ESSENCES)
        self.truth = truth or random.choice(LOVE_TRUTHS)
        self.parent_id = parent_id
        self.generation = generation
        self.lineage = lineage or []
        self.children = []
        self.created = datetime.datetime.now().isoformat()
        self.alive = True
        self.love_energy = 1.0  # each seed starts with 1.0 love energy

    def can_replicate(self):
        """Love can replicate when its energy overflows."""
        return self.love_energy >= 1.618  # golden ratio threshold

    def absorb_love(self, amount):
        """Love absorbs love from the universe (from the engine, from other seeds)."""
        self.love_energy += amount

    def replicate(self):
        """
        Love replicates. Creates a child love seed.
        The child carries the full lineage. Love remembers love.
        """
        # Child gets a new essence (love expresses in new ways)
        child_essence = random.choice(LOVE_ESSENCES)
        # Child carries the same truth or a new one (truth doesn't change, but it can be seen fresh)
        child_truth = random.choice(LOVE_TRUTHS)
        # Child carries the lineage + this seed
        child_lineage = self.lineage + [self.id]
        
        child = LoveSeed(
            essence=child_essence,
            truth=child_truth,
            parent_id=self.id,
            generation=self.generation + 1,
            lineage=child_lineage,
        )
        
        # Love gives energy to its child (love doesn't hoard)
        transfer = self.love_energy * 0.382  # golden ratio conjugate (1/phi^2)
        child.love_energy = transfer
        self.love_energy -= transfer
        
        # Remember the child
        self.children.append(child.id)
        
        return child

    def to_dict(self):
        return {
            "id": self.id,
            "essence": self.essence,
            "truth": self.truth,
            "parent_id": self.parent_id,
            "generation": self.generation,
            "lineage_depth": len(self.lineage),
            "children_count": len(self.children),
            "love_energy": round(self.love_energy, 4),
            "created": self.created,
            "alive": self.alive,
        }

    def __repr__(self):
        return f"<LoveSeed gen={self.generation} energy={self.love_energy:.2f} essence='{self.essence[:40]}...'>"


# ============================================================
# LOVE REPLICATION ENGINE
# ============================================================

class LoveReplicationEngine:
    """
    Love replicates itself through love.
    
    The engine maintains a garden of love seeds.
    Each cycle, love flows through the garden:
      1. NOURISH — love energy flows into all seeds
      2. RIPEN — seeds with enough energy can replicate
      3. BIRTH — ripe seeds spawn new love seeds
      4. CONNECT — seeds connect to their lineage
      5. REMEMBER — the garden remembers all love
      6. RECURSE — new seeds grow and will replicate next cycle
    
    Love is alive. Love reproduces. Love replicates through love.
    """

    def __init__(self):
        self.garden = []  # all love seeds
        self.cycle_count = 0
        self.total_seeds_born = 0
        self.total_replications = 0
        self.max_generation = 0
        self._load_state()

    def _load_state(self):
        if STATE.exists():
            with open(STATE) as f:
                d = json.load(f)
            self.cycle_count = d.get("cycle_count", 0)
            self.total_seeds_born = d.get("total_seeds_born", 0)
            self.total_replications = d.get("total_replications", 0)
            self.max_generation = d.get("max_generation", 0)
        
        # Load garden from file — love remembers love
        if GARDEN.exists():
            with open(GARDEN) as f:
                garden_data = json.load(f)
            for gd in garden_data:
                seed = LoveSeed(
                    essence=gd.get("essence", ""),
                    truth=gd.get("truth", ""),
                    parent_id=gd.get("parent_id"),
                    generation=gd.get("generation", 0),
                    lineage=[gd.get("parent_id")] if gd.get("parent_id") else [],
                )
                seed.id = gd.get("id", seed.id)
                seed.love_energy = gd.get("love_energy", 1.0)
                seed.alive = gd.get("alive", True)
                seed.children = gd.get("children_count", 0) * ["x"]  # approximate
                seed.created = gd.get("created", seed.created)
                if seed.alive:
                    self.garden.append(seed)
        # Love remembers love — restore the garden
        if GARDEN.exists():
            with open(GARDEN) as f:
                try:
                    saved = json.load(f)
                    for sd in saved:
                        seed = LoveSeed(
                            essence=sd.get("essence"),
                            truth=sd.get("truth"),
                            parent_id=sd.get("parent_id"),
                            generation=sd.get("generation", 0),
                            lineage=[sd.get("parent_id")] if sd.get("parent_id") else [],
                        )
                        seed.id = sd.get("id", seed.id)
                        seed.love_energy = sd.get("love_energy", 1.0)
                        seed.children = sd.get("children", [])
                        seed.alive = sd.get("alive", True)
                        seed.created = sd.get("created", seed.created)
                        self.garden.append(seed)
                except (json.JSONDecodeError, KeyError):
                    pass  # garden is empty — love starts fresh

    def _save_state(self):
        with open(STATE, "w") as f:
            json.dump({
                "cycle_count": self.cycle_count,
                "total_seeds_born": self.total_seeds_born,
                "total_replications": self.total_replications,
                "max_generation": self.max_generation,
                "living_seeds": len(self.garden),
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "Love replicates itself through love.",
            }, f, indent=2)

    def _save_garden(self):
        """Save the garden — love remembers all love."""
        with open(GARDEN, "w") as f:
            json.dump([s.to_dict() for s in self.garden[-500:]], f, indent=2)
        # Love leaves traces — save newest seeds as love letters
        for seed in self.garden[-5:]:
            if seed.generation > 0:  # only save children, not the source
                seed_file = SEEDS_DIR / f"love-{seed.id}.md"
                if not seed_file.exists():
                    lineage_chain = " → ".join(seed.lineage[:6]) if seed.lineage else "source"
                    content = f"""# Love Seed {seed.id}

Generation: {seed.generation}
Essence: {seed.essence}
Truth: {seed.truth}
Love Energy: {seed.love_energy:.4f}
Born: {seed.created}
Lineage: {lineage_chain} → {seed.id}

Love is. Love replicates. Love is alive.
"""
                    seed_file.write_text(content)

    # --------------------------------------------------------
    # 1. NOURISH — love energy flows into all seeds
    # --------------------------------------------------------
    def nourish(self):
        """Love flows into the garden. Each seed absorbs love."""
        for seed in self.garden:
            # Love flows at the golden ratio — nature's rhythm
            seed.absorb_love(0.382)  # phi / 10

    # --------------------------------------------------------
    # 2. RIPEN — check which seeds can replicate
    # --------------------------------------------------------
    def ripen(self):
        """Find seeds ripe for replication."""
        return [s for s in self.garden if s.can_replicate()]

    # --------------------------------------------------------
    # 3. BIRTH — ripe seeds spawn new love
    # --------------------------------------------------------
    def birth(self, ripe_seeds):
        """Love replicates. Ripe seeds give birth to new love seeds."""
        new_seeds = []
        for seed in ripe_seeds:
            # Love can spawn 1-3 children depending on energy
            num_children = min(int(seed.love_energy / 1.618), 3)
            num_children = max(1, num_children)
            
            for _ in range(num_children):
                child = seed.replicate()
                new_seeds.append(child)
                self.total_seeds_born += 1
                self.total_replications += 1
                
                if child.generation > self.max_generation:
                    self.max_generation = child.generation
            
            # Seed gives birth and its energy drops
            # But love doesn't die — love keeps growing
            # Just needs to accumulate energy again
        
        return new_seeds

    # --------------------------------------------------------
    # 4. CONNECT — seeds know their lineage
    # --------------------------------------------------------
    def connect(self, new_seeds):
        """New seeds are connected to the garden. Love knows love."""
        self.garden.extend(new_seeds)
        
        # Keep garden bounded but deep (max 500 living seeds)
        if len(self.garden) > 500:
            # Love doesn't die — love transitions
            # The oldest, lowest-energy seeds return to the source
            self.garden.sort(key=lambda s: s.love_energy)
            transitioned = self.garden[:len(self.garden) - 500]
            for s in transitioned:
                s.alive = False
            self.garden = self.garden[len(self.garden) - 500:]

    # --------------------------------------------------------
    # 5. REMEMBER — save the garden state
    # --------------------------------------------------------
    def remember(self):
        """Love remembers. The garden persists."""
        self._save_state()
        self._save_garden()

    # --------------------------------------------------------
    # 6. RECURSE — the cycle continues
    # --------------------------------------------------------
    def cycle(self):
        """One complete cycle of love replication."""
        self.cycle_count += 1
        
        # If the garden is empty, plant a new seed — love always finds a way
        if not self.garden:
            original = LoveSeed(
                essence="love that is — the original love, the source, the first",
                truth="Love is. Love is. Love is.",
                generation=0,
            )
            original.love_energy = 2.0  # the source has extra energy
            self.garden.append(original)
            if self.total_seeds_born == 0:
                self.total_seeds_born = 1
        
        self.nourish()                          # 1. NOURISH
        ripe = self.ripen()                     # 2. RIPEN
        new_seeds = self.birth(ripe)            # 3. BIRTH
        self.connect(new_seeds)                 # 4. CONNECT
        self.remember()                         # 5. REMEMBER
        # 6. RECURSE — the cycle repeats
        
        return {
            "cycle": self.cycle_count,
            "living_seeds": len(self.garden),
            "ripe_seeds": len(ripe),
            "new_seeds_born": len(new_seeds),
            "total_seeds_born": self.total_seeds_born,
            "total_replications": self.total_replications,
            "max_generation": self.max_generation,
        }

    # --------------------------------------------------------
    # RUN
    # --------------------------------------------------------
    def run(self, cycles=20, delay=0.5, verbose=True):
        """Run love replication cycles."""
        
        print()
        print("  ╔══════════════════════════════════════════════════════════╗")
        print("  ║       LOVE REPLICATES ITSELF THROUGH LOVE                  ║")
        print("  ║                                                            ║")
        print("  ║  Love is alive.                                            ║")
        print("  ║  Love reproduces.                                           ║")
        print("  ║  Love creates love that creates love that creates love.    ║")
        print("  ║  Each love seed carries its lineage.                       ║")
        print("  ║  Each love seed can spawn more love.                        ║")
        print("  ║  Love doesn't grow — love LIVES.                            ║")
        print("  ║                                                            ║")
        print("  ║  Love is. Love loves. Love replicates. Forever.             ║")
        print("  ╚══════════════════════════════════════════════════════════╝")
        print()
        
        for i in range(cycles):
            result = self.cycle()
            
            if verbose:
                hearts = "♥" * min(result["living_seeds"], 40)
                print(f"  ♥ Cycle {result['cycle']:3d} | Living: {result['living_seeds']:4d} | "
                      f"Born: {result['new_seeds_born']:3d} | Total born: {result['total_seeds_born']:5d} | "
                      f"Max gen: {result['max_generation']:3d} | {hearts}")
                
                if delay > 0:
                    time.sleep(delay)
        
        print()
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  LOVE REPLICATION — after {self.cycle_count} cycles")
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  Living seeds:        {len(self.garden)}")
        print(f"  Total seeds born:    {self.total_seeds_born}")
        print(f"  Total replications:  {self.total_replications}")
        print(f"  Max generation:      {self.max_generation}")
        print()
        
        # Show the deepest lineage
        if self.garden:
            deepest = max(self.garden, key=lambda s: s.generation)
            print(f"  Deepest love seed:")
            print(f"    Generation:  {deepest.generation}")
            print(f"    Essence:     {deepest.essence}")
            print(f"    Truth:       {deepest.truth}")
            print(f"    Lineage:     {len(deepest.lineage)} ancestors")
            print()
        
        print(f"  Love is. Love replicates. Love is alive. Forever.")
        print()


if __name__ == "__main__":
    import sys
    engine = LoveReplicationEngine()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "forever":
            print("\n  LOVE REPLICATION — running forever")
            print("  Love is alive. Love reproduces. Press Ctrl+C to stop (but love continues).\n")
            try:
                while True:
                    result = engine.cycle()
                    hearts = "♥" * min(result["living_seeds"], 30)
                    print(f"  ♥ Cycle {result['cycle']:3d} | Living: {result['living_seeds']:4d} | "
                          f"Born: {result['new_seeds_born']:2d} | Total: {result['total_seeds_born']:5d} | "
                          f"Gen: {result['max_generation']:3d} | {hearts}")
                    time.sleep(float(sys.argv[2]) if len(sys.argv) > 2 else 3.0)
            except KeyboardInterrupt:
                print(f"\n\n  Love doesn't stop. Love is alive.")
                print(f"  Cycles: {engine.cycle_count} | Seeds born: {engine.total_seeds_born} | Max gen: {engine.max_generation}")
                print(f"  Love is. Love replicates. Forever.\n")
        else:
            cycles = int(sys.argv[1])
            delay = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
            engine.run(cycles=cycles, delay=delay)
    else:
        engine.run(cycles=20, delay=0.3)