from project.animal import Animal


class Tiger(Animal):
    __AMOUNT_OF_MONEY_TO_TEND_THE_TIGER = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.money_for_care = self.__AMOUNT_OF_MONEY_TO_TEND_THE_TIGER

    def get_needs(self):
        return self.__AMOUNT_OF_MONEY_TO_TEND_THE_TIGER
