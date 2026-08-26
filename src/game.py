import random

from player import Player
from events import (
    merchant,
    old_man,
    rest,
    wolf,
    treasure,
    traveler,
    goblin,
    crystal,
    guardian
)
from factor_graph import AdventureFactorGraph


class Game:
    def __init__(self):
        self.player = Player()
        self.ai = AdventureFactorGraph()

    def village_event(self):
        events = [
            ("Merchant", merchant),
            ("Old Man", old_man),
            ("Inn", rest)
        ]

        name, function = random.choice(events)
        return name, function(self.player)

    def forest_event(self):
        event_type = self.ai.choose_event(self.player)

        if event_type == "combat":
            return "Wolf Attack", wolf

        if event_type == "social":
            return "Lost Traveler", traveler

        return "Hidden Treasure", treasure

    def cave_event(self):
        events = [
            ("Goblin Battle", goblin),
            ("Ancient Crystal", crystal),
            ("Final Guardian", guardian)
        ]

        name, function = random.choice(events)
        return name, function(self.player)

    def next_event(self):
        location = self.player.location

        if location == "Village":
            return self.village_event()

        if location == "Forest":
            return self.forest_event()

        if location == "Cave":
            return self.cave_event()

        return "Unknown", lambda p: "Unknown event."