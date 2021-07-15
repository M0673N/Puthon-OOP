class Shop:
    def __init__(self, name, type_, capacity):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def small_shop(cls, name, type_):
        return cls(name, type_, 10)

    def check_capacity(self):
        return sum([self.items[items] for items in self.items])

    def add_item(self, item_name):
        if self.check_capacity() >= self.capacity:
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the shop"
