class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = f"Name: {self.name}\n" \
                 f"Guild: {self.guild}\n" \
                 f"HP: {self.hp}\n" \
                 f"MP: {self.mp}\n"
        for skill in self.skills:
            result += f"==={skill} - {self.skills[skill]}\n"
        result.rstrip()
        return result
