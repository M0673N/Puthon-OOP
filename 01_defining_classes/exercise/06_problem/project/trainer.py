class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon:
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            result += f"- {pokemon.pokemon_details()}\n"
        result.rstrip()
        return result
