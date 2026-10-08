import time
import random

class Character :
    def __init__(self, name, health, special_item):
        self.name= name
        self.health = health
        self.sp = special_item

    def is_alive(self):
        if self.health > 0:
            return True
        else :
            return False
        
    def special_i(self):
        if self.sp == "berserker posion":
            return 50
        elif self.sp == "spike posion":
            return 50
        elif self.sp == "reflect posion" :
            return 70

class Warrior(Character):

    def __init__(self, name, health, special_item):
        super().__init__(name, health, special_item)

    @property
    def is_alive(self):
        return super().is_alive()

    def set_1(self):
        return [("slash", 60), ("charge", 130)]
    def set_2(self):
        return [("charge", 130),("concentrated pierce" , 150)]
    
    @property
    def special_i(self):
        return super().special_i()
        
class Mage(Character):
    def __init__(self, name, health, special_item):
        super().__init__(name, health, special_item)
    @property
    def is_alive(self):
        return super().is_alive()
    def set_1(self):
        return [("fire", 55), ("ice shards", 135 )]
    def set_2(self):
        return [("ice shards", 135),("light beam" , 155)]
    @property
    def special_i(self):
        return super().special_i()
        
class Archer(Character):
    def __init__(self, name, health, special_item):
        super().__init__(name, health, special_item)

    @property
    def is_alive(self):
        return super().is_alive()
    def set_1(self):
        return [("arrow", 70), ("fire arrow", 126)]
    def set_2(self):
        return [("fire arrow", 126),("arrow rain" , 150)]
    @property
    def special_i(self):
        return super().special_i()

class Battle():
    def __init__(self, w1,w2):
        self.player1 = w1
        self.player2 = w2

    def battle_start(self):
        round = 1
        print(
              f"The Battle Between {self.player1.name} & {self.player2.name}\n"
        )
        time.sleep(2)
        print(f"Begins Now\n")
        while True :
            if self.player1.is_alive and self.player2.is_alive :
                pass
            else :
                if self.player1.is_alive:
                    print(f"{self.player1.name} : hp {self.player1.health} & {self.player2.name} : hp 0")
                    print(f"{self.player1.name} won")
                    break
                elif self.player2.is_alive :
                    print(f"{self.player1.name} : hp 0 & {self.player2.name} : hp {self.player2.health}")
                    print(f"{self.player2.name} won")
                    break

            print(f"round: {round}\n")
            print(f"hp : {self.player1.name} {self.player1.health}, {self.player2.name} {self.player2.health} ")
            if round < 3 :
                atk_p1 = random.choice(self.player1.set_1())
                atk_p2 = random.choice(self.player2.set_1())

            else :
                atk_p1 = random.choice(self.player1.set_2())
                atk_p2 = random.choice(self.player2.set_2())

            print(f"atack : {self.player1.name}-{atk_p1[0]}, damage: {atk_p1[1]}"
                  f"atack : {self.player2.name}-{atk_p2[0]}, damage: {atk_p2[1]}\n")
            
            if round == 3:
                sp_1= self.player1.special_i
                sp_2= self.player2.special_i
                print(f"{self.player1.name} used {self.player1.sp}")
                print(f"{self.player2.name} used {self.player2.sp}\n")
                self.player1.health = self.player1.health - atk_p2[1] - sp_2
                self.player2.health = self.player2.health - atk_p1[1] - sp_1

            else:
                self.player1.health = self.player1.health - atk_p2[1] 
                self.player2.health = self.player2.health - atk_p1[1]
            round +=1
    


Warrior1 = Warrior("draco", 600, "berserker posion")
Archer1 = Archer("michell", 500, "spike posion")

Battle1 = Battle(Warrior1,Archer1)

Battle1.battle_start()