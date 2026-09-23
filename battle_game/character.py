class Character:
    def __init__(self, health, damage, weapon):
        self._health = health
        self.damage = damage
        self.weapon = weapon

    def attack(self, enemy):
        total_damage = self.damage + self.weapon.damage
        enemy.take_damage(total_damage)

    def take_damage(self, damage):
        self._health -= damage

        if self._health < 0:
            self._health = 0

    def is_alive(self):
        return self._health > 0

    def get_health(self):
        return self._health

#Родительский класс + инкапсуляция