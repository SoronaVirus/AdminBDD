import random
#Classe des personnages
class Character:

    def __init__(self, name, attack, armor, hp, crit_chance, evasion):
        self.name = name
        self.attack_power = attack
        self.armor = armor
        self.hp = hp
        self.hp_max = hp
        self.crit_chance = crit_chance
        self.evasion = evasion

        self.crit_multiplier = 2

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        is_critical = random.randint(1,100) <= self.crit_chance

        if is_critical:
            damage = max(0, (self.attack_power * self.crit_multiplier) - target.armor)
            target.hp -= damage
            return damage, True
        else:
            base_damage = max(0, self.attack_power - target.armor)
            target.hp -= base_damage
            return base_damage, False
    
    def __str__(self):
        current_hp = max(0, self.hp)
        return f"{self.name} - ATK: {self.attack_power}, DEF: {self.armor}, HP: {current_hp}/{self.hp_max}, CRIT: {self.crit_chance}%, EVA: {self.evasion}%"
    
#Classe des monstres
class Monster:

    def __init__(self, name, attack, armor, hp):
        self.name = name
        self.attack_power = attack
        self.armor = armor
        self.hp = hp
        self.hp_max = hp

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        if random.randint(1,100) <= target.evasion:
            return 0, False
        
        damage = max(0, self.attack_power - target.armor)
        target.hp -= damage
        return damage, True
    
    def __str__(self):
        current_hp = max(0, self.hp)
        return f"{self.name} - ATK: {self.attack_power}, DEF: {self.armor}, HP: {current_hp}/{self.hp_max}"
    
#Classe des objets ???