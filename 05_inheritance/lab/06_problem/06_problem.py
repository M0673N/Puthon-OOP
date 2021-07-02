class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        result = reversed(self.data)
        return f"[{', '.join(result)}]"

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False
