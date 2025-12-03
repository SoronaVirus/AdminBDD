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

    def __init__(self, name, attack, armor, hp, crit_chance, evasion):
        super().__init__(name, attack, armor, hp)
        self.crit_chance = crit_chance
        self.evasion = evasion
        self.crit_multiplier = 2
    
    def attack(self, target):
        is_critical = random.randint(1,100) <= self.crit_chance

        if is_critical:
            damage = max(0, (self.attack_power * self.crit_multiplier) - target.armor)
        else:
            damage = max(0, self.attack_power - target.armor)

        target.take_damage(damage)
        return damage, is_critical
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, CRIT: {self.crit_chance}%, EVA: {self.evasion}%"
    
#Classe des monstres
class Monster(Entity):
    
    def attack(self, target):
        if random.randint(1,100) <= target.evasion:
            return 0, False
        
        damage = max(0, self.attack_power - target.armor)
        target.take_damage(damage)
        return damage, True

#Classe des objets ???