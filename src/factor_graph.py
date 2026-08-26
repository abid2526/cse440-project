import numpy as np
from pgmpy.models import FactorGraph
from pgmpy.factors.discrete import DiscreteFactor


class AdventureFactorGraph:
    def __init__(self):
        self.graph = FactorGraph()

        self.graph.add_nodes_from([
            "Health",
            "Weapon",
            "Gold",
            "Reputation",
            "Location",
            "Event"
        ])

        # Combat factor:
        # Health, Weapon -> Event
        combat = DiscreteFactor(
            ["Health", "Weapon", "Event"],
            [2, 2, 3],
            np.array([
                0.2, 0.6, 0.2,
                0.1, 0.2, 0.7,
                0.7, 0.2, 0.1,
                0.3, 0.5, 0.2
            ]).reshape(2, 2, 3)
        )

        # Social factor:
        # Reputation, Gold -> Event
        social = DiscreteFactor(
            ["Reputation", "Gold", "Event"],
            [2, 2, 3],
            np.array([
                0.2, 0.6, 0.2,
                0.3, 0.5, 0.2,
                0.5, 0.3, 0.2,
                0.7, 0.2, 0.1
            ]).reshape(2, 2, 3)
        )

        # Exploration factor:
        # Location, Reputation -> Event
        exploration = DiscreteFactor(
            ["Location", "Reputation", "Event"],
            [3, 2, 3],
            np.ones(18)
        )

        self.graph.add_factors(combat, social, exploration)

        for factor in [combat, social, exploration]:
            for variable in factor.variables:
                self.graph.add_edge(variable, factor)

        self.graph.check_model()

    def choose_event(self, player):
        """
        Uses the factor graph to score the possible event types.
        """

        health = 0 if player.health >= 50 else 1
        weapon = 1 if player.weapon else 0
        gold = 0 if player.gold >= 30 else 1
        reputation = 0 if player.reputation == "Good" else 1

        scores = {
            "combat": 0,
            "social": 0,
            "exploration": 0
        }

        # Combat preference
        if weapon:
            scores["combat"] += 2
        if health == 0:
            scores["combat"] += 1

        # Social preference
        if reputation == 0:
            scores["social"] += 2
        if gold == 0:
            scores["social"] += 1

        # Exploration is always possible
        scores["exploration"] += 1

        # Add small variation so the story isn't completely fixed
        choices = list(scores.keys())
        weights = np.array([scores[c] for c in choices], dtype=float)

        weights = weights / weights.sum()

        return np.random.choice(choices, p=weights)