class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        num = self.count
        if num < 0:
            raise StopIteration
        self.count -= 1
        return num


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
