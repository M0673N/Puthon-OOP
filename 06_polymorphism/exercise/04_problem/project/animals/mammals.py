from project.animals.animal import Mammal


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.1


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == "Seed":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.3


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * 1
