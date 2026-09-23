from characters.orc import Orc
from characters.elf import Elf
from characters.dwarf import Dwarf
from characters.human import Human


class CharacterFactory:
    @staticmethod
    def create_character(race):
        if race == "orc":
            return Orc()

        if race == "elf":
            return Elf()

        if race == "dwarf":
            return Dwarf()

        if race == "human":
            return Human()

        raise ValueError("Неизвестная раса")

#Фабрика паттерн