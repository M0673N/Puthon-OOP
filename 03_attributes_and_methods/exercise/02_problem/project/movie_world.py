class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        capacity = 15
        return capacity

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def get_customer_from_id(self, customer_id):
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        return customer

    def get_dvd_from_id(self, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        return dvd

    def rent_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd_from_id(dvd_id)
        customer = self.get_customer_from_id(customer_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd_from_id(dvd_id)
        customer = self.get_customer_from_id(customer_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += str(customer) + "\n"
        result.rstrip()
        for dvd in self.dvds:
            result += str(dvd) + "\n"
        result.rstrip()
        return result
