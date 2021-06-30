from project.animal import Animal


class Tiger(Animal):
    __AMOUNT_OF_MONEY_TO_TEND_THE_TIGER = 45

    def get_needs(self):
        return self.__AMOUNT_OF_MONEY_TO_TEND_THE_TIGER
