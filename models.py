import random

#Classe des entités
class Entity:
    def __init__(self, name, attack, armor, hp):
        self.name = name
        self.attack_power = attack
        self.armor = armor
        self.hp = hp
        self.hp_max = hp

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= damage

    def __str__(self):
        current_hp = max(0, self.hp)
        return f"{self.name} - ATK: {self.attack_power}, DEF: {self.armor}, HP: {current_hp}/{self.hp_max}"
    
#Classe des personnages
class Character(Entity):

    def __init__(self, name, attack, armor, hp, crit_chance, evasion, lifesteal, thorns):
        super().__init__(name, attack, armor, hp)
        self.crit_chance = crit_chance
        self.evasion = evasion
        self.lifesteal = lifesteal
        self.thorns = thorns
        self.crit_multiplier = 2
    
    def attack(self, target):
        is_critical = random.randint(1,100) <= self.crit_chance

        if is_critical:
            damage = round(max(0, (self.attack_power * self.crit_multiplier) - target.armor))
        else:
            damage = max(0, self.attack_power - target.armor)

        target.take_damage(damage)

        if self.lifesteal > 0 and damage > 0:
            heal_amount = round(damage * (self.lifesteal / 100))
            if heal_amount > 0:
                self.hp = min(self.hp + heal_amount, self.hp_max)

        return damage, is_critical
    
    def __str__(self):
        base_str = super().__str__()
        stats = f"{base_str}, CRIT: {self.crit_chance}%, EVA: {self.evasion}%"

        if self.lifesteal > 0:
            stats += f", LIFESTEAL: {self.lifesteal}%"

        if self.thorns > 0:
            stats += f", THORNS: {self.thorns}%"

        return stats
    
#Classe des monstres
class Monster(Entity):
    
    def attack(self, target):
        if random.randint(1,100) <= target.evasion:
            return 0, False, 0
        
        damage = max(0, self.attack_power - target.armor)
        target.take_damage(damage)

        thorns_damage = 0
        if target.thorns > 0 and damage > 0:
            thorns_damage = round(damage * (target.thorns / 100))
            if thorns_damage > 0:
                self.take_damage(thorns_damage)

        return damage, True, thorns_damage