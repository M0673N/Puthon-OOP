class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.count_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_2 == self.count:
            raise StopIteration
        num = self.num
        self.num += 1
        if num % self.step == 0:
            self.count_2 += 1
            return num
        return self.__next__()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
