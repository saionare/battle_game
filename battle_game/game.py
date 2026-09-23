class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.characters = []

        return cls._instance

    def add_character(self, character):
        self.characters.append(character)

    def get_characters(self):
        return self.characters

    def clear(self):
        self.characters.clear()

#Синглтон паттерн