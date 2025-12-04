import random
from utils import get_connection, print_title

reset_color = "\033[0m"

def get_all_effects():
    db = get_connection()
    effects = {}
    for effect in db.effects.find():
        effects[effect['key']] = {
            "name": effect['name'],
            "stat": effect['stat'],
            "values": effect['values'],
            "description": effect['description']
        }
    return effects

def get_all_rarities():
    db = get_connection()
    rarities = {}
    for rarity in db.rarities.find():
        rarities[rarity['name']] = {
            "weight": rarity['weight'],
            "color": rarity['color']
        }
    return rarities

def get_random_rarity():
    rarities_data = get_all_rarities()
    rarities = list(rarities_data.keys())
    weights = [rarities_data[r]["weight"] for r in rarities]

    return random.choices(rarities, weights=weights)[0]

def generate_effect():
    effects_data = get_all_effects()
    effect_key = random.choice(list(effects_data.keys()))
    rarity = get_random_rarity()
    effect = effects_data[effect_key]

    return {
        "key": effect_key,
        "name": effect["name"],
        "stat": effect["stat"],
        "value": effect["values"][rarity],
        "rarity": rarity,
        "description": effect["description"]
    }

def generate_three_effects():
    effects = []
    used_keys = set()
    
    while len(effects) < 3:
        effect = generate_effect()
        if effect["key"] not in used_keys:
            effects.append(effect)
            used_keys.add(effect["key"])
    
    return effects

def print_effects(effects):
    rarities_data = get_all_rarities()
    
    print_title("A gift is here for your team")
    print("\nSelect one effect :\n")
    
    for i, effect in enumerate(effects, 1):
        color = rarities_data[effect["rarity"]]["color"]
        
        if effect["stat"] == "crit_multiplier":
            value_str = f"+{effect['value']:.1f}x"
        elif effect["stat"] in ["evasion", "crit_chance", "lifesteal", "thorns"]:
            value_str = f"+{effect['value']}%"
        else:
            value_str = f"+{int(effect['value'])}"
        
        print(f"{i}. {color}[{effect['rarity']}]{reset_color} {effect['name']}")
        print(f"{effect['description']}: {value_str}\n")

def apply_effect_to_team(team, effect):
    rarities_data = get_all_rarities()
    
    for character in team:
        if character.is_alive():
            if effect["stat"] == "hp":
                character.hp = min(character.hp + effect["value"], character.hp_max)
            else:
                current_value = getattr(character, effect["stat"])
                setattr(character, effect["stat"], current_value + effect["value"])
    
    color = rarities_data[effect["rarity"]]["color"]
    print(f"\n{color}[{effect['rarity']}]{reset_color} {effect['name']} applied on your whole team.")