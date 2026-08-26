def merchant(player):
    if player.gold >= 20 and not player.weapon:
        player.gold -= 20
        player.weapon = True
        return "You bought a sword for 20 gold."
    elif player.weapon:
        return "You already have a sword."
    else:
        return "You do not have enough gold for a sword."


def old_man(player):
    player.reputation = "Good"
    return "The old man gives you advice about the forest."


def rest(player):
    player.health = min(100, player.health + 30)
    return "You rested at the inn and recovered some health."


def wolf(player):
    if player.weapon:
        player.health -= 10
        player.gold += 10
        return "You defeated the wolf because you had a weapon. You gained 10 gold."
    else:
        player.health -= 40
        return "The wolf attacked you. You had no weapon and lost 40 health."


def treasure(player):
    player.gold += 25
    return "You found a hidden treasure containing 25 gold."


def traveler(player):
    player.reputation = "Good"
    player.gold += 10
    return "You helped the lost traveler. Your reputation improved and you received 10 gold."


def goblin(player):
    if player.weapon:
        player.health -= 15
        return "You defeated the goblin with your sword."
    else:
        player.health -= 50
        return "The goblin injured you badly because you had no weapon."


def crystal(player):
    player.crystal = True
    return "You found the Ancient Crystal!"


def guardian(player):
    if player.weapon and player.health >= 40:
        player.health -= 20
        player.crystal = True
        return "You defeated the Final Guardian and obtained the Ancient Crystal!"
    else:
        player.health = 0
        return "The Final Guardian was too strong. You were defeated."