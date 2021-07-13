sounds_database = {"cat": "meow", "dog": "woof-woof", "chicken": "the sound that chickens make"}


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def make_sound(self, mapper):
        print(mapper[self.species])


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound(sounds_database)


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
