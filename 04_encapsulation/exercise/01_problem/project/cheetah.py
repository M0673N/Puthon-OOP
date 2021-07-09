from project.animal import Animal


class Cheetah(Animal):
    __AMOUNT_OF_MONEY_TO_TEND_THE_CHEETAH = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.money_for_care = self.__AMOUNT_OF_MONEY_TO_TEND_THE_CHEETAH

    def get_needs(self):
        return self.__AMOUNT_OF_MONEY_TO_TEND_THE_CHEETAH
