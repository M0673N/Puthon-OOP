class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary = dictionary_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1
        if index >= len(self.dictionary):
            raise StopIteration
        return list(self.dictionary.items())[index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
