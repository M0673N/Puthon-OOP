class Customer:
    id = 1

    def __init__(self, name, address, email_address):
        self.name = name
        self.address = address
        self.email = email_address
        self.id = Customer.id
        Customer.id += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.id