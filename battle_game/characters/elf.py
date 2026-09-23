from character import Character
from weapon import Weapon
class Elf(Character):
    def __init__(self):
        weapon = Weapon("Лук", 10)
        super().__init__(90, 30, weapon)

    def attack(self, enemy):
        damage = self.damage + self.weapon.damage + 10
        enemy.take_damage(damage)
        print(f"Эльф атакует и наносит {damage} урона")

#Наследование + полиморфизм