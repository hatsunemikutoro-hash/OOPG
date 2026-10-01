import random
import time
from enemy import Enemy
from player import Player
from utils import roll

class Game:
    def __init__(self):
        self.player = Player(100, 100)
        self.running = True
        self.inBattle = False

        self.biomes = ["Temperate Forest", "Boreal Forest", "Jungle",
                       "Hot Desert", "Rocky Badlands", "Tundra", "Glacial Wastes",
                       ]

        self.enemys = [Enemy("Zombie", 25, 100)]
        self.oponent = None
    def explore(self):
        biome = random.choice(self.biomes)
        print("The Player goes for an adventure ...")
        time.sleep(0.5)
        print(f"The Player goes inside the {biome} ...")
        time.sleep(0.5)

        probrality = roll(20)

        if probrality > 10:
            self.inBattle = True
            self.oponent = random.choice(self.enemys)
            print(f"The Player finds and {self.oponent.name}")
        else:
            print(f"And doesn't find nothing ... | HP : {self.player.life}")

    def viewInv(self):
        print(f"Level: {self.player.level} XP: {self.player.xp} / {self.player.life}")
        print(f"You have {self.player.potions} potions !!")

    def notInBat(self):
        turn = str(input("(e) Explore (h) Heal (i) Inventory: "))

        turn = turn.strip().lower()
        if turn == "e":
                self.explore()

        if turn == "h":
                self.player.healed()

        if turn == "i":
                self.viewInv()

    def battle(self):
        print(f"Player HP: {self.player.life} | Enemy HP {self.oponent.life}")
        action = input("(a) Attack (d) Defend (h) Heal: ").strip().lower()

        if action == 'a':
            result = self.oponent.getDamage(self.player.str)

            proba_hit = roll(20)

            if proba_hit > 8:
                print(f"{self.oponent.name} strikes you with {self.oponent.strength} damage!")
                self.player.getDmg(self.oponent.strength)

            if self.player.life < 0:
                print("You died!")
                self.oponent = None
                self.inBattle = False

            if result == 0:
                xp = random.randint(1, self.player.level + 3 * 5)
                print(f"{self.oponent.name} got defeated !! got {xp}")
                print("="*40)

                coiso = self.player.get_xp(xp)

                if coiso is not None:
                    print(coiso)

                print(f"{self.player.xp} / {self.player.max_xp} XP")
                print("="*40)
                self.inBattle = False
                self.oponent = None

    def run(self):
        while self.running:
            if not self.inBattle:
                self.notInBat()

            if self.inBattle:
                self.battle()


game = Game()
game.run()