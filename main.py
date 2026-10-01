import random
import time
from enemy import Enemy
from player import Player

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

        probrality = random.randint(1, 20)

        if probrality > 10:
            self.inBattle = True
            self.oponent = random.choice(self.enemys)
            print(f"The Player finds and {self.oponent.name}")
        else:
            print(f"And doesn't find nothing ... | HP : {self.player.life}")

    def viewInv(self):
        print(f"You have {self.player.potions} potions !!")

    def run(self):
        while self.running:
            if not self.inBattle:
                turn = str(input("(e) Explore (h) Heal (i) Inventory: "))

                turn = turn.strip().lower()
                if turn == "e":
                    self.explore()

                if turn == "h":
                    self.player.healed()

                if turn == "i":
                    self.viewInv()
            else:
                print(f"Player HP: {self.player.life} | Enemy HP {self.oponent.life}")

                action = input("(a) Attack (d) Defend (h) Heal: ")


game = Game()
game.run()