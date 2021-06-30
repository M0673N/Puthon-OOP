from project.animal import Animal


class Lion(Animal):
    __AMOUNT_OF_MONEY_TO_TEND_THE_LION = 50

    def get_needs(self):
        return self.__AMOUNT_OF_MONEY_TO_TEND_THE_LION
