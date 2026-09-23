from character import Character
from weapon import Weapon
class Dwarf(Character):
    def __init__(self):
        weapon = Weapon("Молот", 12)
        super().__init__(140, 20, weapon)

    def attack(self, enemy):
        damage = self.damage + self.weapon.damage + 8
        enemy.take_damage(damage)
        print(f"Гном атакует и наносит {damage} урона")

#Наследование + полиморфизм