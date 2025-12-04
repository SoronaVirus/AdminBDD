# Surviving Game

A turn-based combat game where you build a team of characters to survive waves of monsters.

## Installation

Install the required dependencies:

```bash
pip install pymongo
```

Make sure MongoDB is running on your local machine (`localhost:27017`).

## How to Play

1. **Initialize the database** (first time only):
   ```bash
   python db_init.py
   ```

2. **Launch the game**:
   ```bash
   python main.py
   ```

## New Features

### EVA (Evasion)
Characters can now dodge monster attacks based on their evasion stat. Higher evasion means more chances to avoid damage completely.

### Critical Hits
Characters have a critical hit chance that deals increased damage (2x multiplier by default). The critical multiplier can be boosted through effects.

### Effects and Rarity
Every 10 attacks, choose one of three random effects to boost your team. Effects come in different rarities (Common, Rare, Epic, Exotic, Legendary) with higher rarities providing stronger bonuses.

## Gameplay

1. Select 3 characters for your team
2. Fight waves of increasingly difficult monsters
3. Gain effects every 10 attacks to power up your team
4. Survive as many waves as possible!

Your score is saved to the leaderboard when you lose.