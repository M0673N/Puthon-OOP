from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_number = 0
        self.deque = deque(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        num = self.current_number
        self.current_number += 1
        if num == self.number:
            raise StopIteration
        deque_ = self.deque
        self.deque.rotate(-1)
        return deque_[-1]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
