#Classe des personnages
class Character:

    def __init__(self, name, attack, armor, hp):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.hp = hp
        self.hp_max = hp

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        damage = max(0, self.attack - target.armor)
        target.hp -= damage
        return damage
    
    def attack_taken(self, damage):
        damage_taken = max(0, damage - self.armor)
        self.hp -= damage_taken
        return damage_taken
    
    def __str__(self):
        return f"{self.name} - ATK: {self.attack}, DEF: {self.armor}, HP: {self.hp}/{self.hp_max}"
    
#Classe des monstres
class Monster:

    def __init__(self, name, attack, armor, hp):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.hp = hp
        self.hp_max = hp

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        damage = max(0, self.attack - target.armor)
        target.hp -= damage
        return damage
    
    def __str__(self):
        return f"{self.name} - ATK: {self.attack}, DEF: {self.armor}, HP: {self.hp}/{self.hp_max}"
    
#Classe des objets ???