from character import Character
from weapon import Weapon
class Human(Character):
    def __init__(self):
        weapon = Weapon("Меч", 10)
        super().__init__(100, 25, weapon)

    def attack(self, enemy):
        damage = self.damage + self.weapon.damage + 3
        enemy.take_damage(damage)
        print(f"Человек атакует и наносит {damage} урона")

#Наследование + полиморфизм