# Factor Graph Design

## Introduction

The main AI component of this project is the Factor Graph. It is used to make decisions during the game instead of relying on a fixed sequence of events.

Rather than checking only one condition, the Factor Graph considers several player variables together before deciding what should happen next. This makes the game more dynamic because different player states can lead to different events.

---

## Variable Nodes

The Factor Graph uses the following player variables:

| Variable   | Possible Values         |
| ---------- | ----------------------- |
| Health     | High / Low              |
| Gold       | High / Low              |
| Weapon     | Yes / No                |
| Reputation | Good / Bad              |
| Location   | Village / Forest / Cave |

These variables represent the current state of the player and are updated throughout the game.

---

## Factor Nodes

To keep the project simple, the Factor Graph is divided into three main factors.

### Combat Factor

Inputs:

- Health
- Weapon

Purpose:
Determines whether the player is likely to win or lose a battle.

Example:
A player with high health and a weapon has a better chance of winning than a player with low health and no weapon.

---

### NPC Interaction Factor

Inputs:

- Gold
- Reputation

Purpose:
Determines how non-player characters (NPCs) respond to the player.

Example:
A player with a good reputation may receive help or discounts, while a player with a bad reputation may be ignored.

---

### Exploration Factor

Inputs:

- Location
- Reputation

Purpose:
Determines which event the player experiences while exploring.

Example:
While exploring the forest, one player may discover hidden treasure, while another may encounter a wolf depending on their current state.

---

## Decision Process

The game follows these steps whenever a new event is needed:

1. Read the player's current state.
2. Send the player variables to the Factor Graph.
3. Evaluate the relevant factor.
4. Select the next event.
5. Update the player's state after the event.

This process repeats until the player reaches one of the game endings.

---

## Example

Player State

- Health = High
- Weapon = Yes
- Reputation = Good
- Location = Forest

Possible Events

- Wolf Attack
- Hidden Treasure
- Lost Traveler

The Factor Graph evaluates the player's current state and selects one of these events. Different player states may result in different outcomes, making the story more dynamic.

---

## Future Implementation

During the implementation phase, the Factor Graph will be developed using the `pgmpy` library. It will be connected to the game logic so that every important decision is made based on the player's current state rather than a fixed storyline.
