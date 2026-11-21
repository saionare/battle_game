import random
from factory import CharacterFactory
from game import Game


game = Game()

orc = CharacterFactory.create_character("orc")
elf = CharacterFactory.create_character("elf")
dwarf = CharacterFactory.create_character("dwarf")
human = CharacterFactory.create_character("human")

game.add_character(orc)
game.add_character(elf)
game.add_character(dwarf)
game.add_character(human)
random.shuffle(game.characters)

print("УЧАСТНИКИ")

for character in game.get_characters():
    print(
        f"{character.__class__.__name__}: "
        f"здоровье = {character.get_health()}, "
        f"оружие = {character.weapon}"
    )

print("\n БОЙ")

characters = game.get_characters()

while len([c for c in characters if c.is_alive()]) > 1:
    for attacker in characters:
        if not attacker.is_alive():
            continue

        enemies = [
            c for c in characters
            if c is not attacker and c.is_alive()
        ]

        if not enemies:
            break

        enemy = random.choice(enemies)

        attacker.attack(enemy)

        print(
            f"У {enemy.__class__.__name__} "
            f"осталось {enemy.get_health()} HP\n"
        )

        if len([c for c in characters if c.is_alive()]) <= 1:
            break

print("РЕЗУЛЬТАТ")

for character in characters:
    if character.is_alive():
        print(
            f"Победитель: {character.__class__.__name__}"
        )

#Запуск игры
