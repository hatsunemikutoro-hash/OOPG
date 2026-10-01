class Player:
    def __init__(self, life, estamina):
        self.life = life
        self.estamina = estamina

        self.potions = 5

    def getDmg(self, dmg):
        self.life -= dmg

    def healed(self):
        if self.potions > 0:
            if self.life + 25 > 100:
                self.life = self.life
                print("Your life is full !!")

            else:
                self.potions -= 1
                self.life += 25
                print(f"You life is now up by +25 | HP : {self.life}")
        else:
            print("You doesn't have potions !!")

        if self.potions < 0:
            self.potions = 0
