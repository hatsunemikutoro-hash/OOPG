class Enemy:
    def __init__(self, name, strength, life):
        self.name = name
        self.strength = strength
        self.life = life

    def getDamage(self, dmg):
        if self.life == 0:
            return 0
        else:
            self.life -= dmg