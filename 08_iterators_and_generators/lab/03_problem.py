class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

        # for chr in self.string:
        #     if chr.lower() in "aeiouy":
        #         yield chr

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        if char.lower() in "aeiouy":
            return char
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
