from project.animals.animal import Bird


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.25


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35
