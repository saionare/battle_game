from character import Character
from weapon import Weapon
class Orc(Character):
    def __init__(self):
        weapon = Weapon("Топор", 15)
        super().__init__(120, 25, weapon)

    def attack(self, enemy):
        damage = self.damage + self.weapon.damage + 5
        enemy.take_damage(damage)
        print(f"Орк атакует и наносит {damage} урона")

#Наследование + полиморфизм