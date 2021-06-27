class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_from_id(id, collection):
        for item in collection:
            if id == item.id:
                return item

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_from_id(subscription_id, self.subscriptions)
        result = ""
        result += str(subscription) + "\n"
        customer_id = subscription.customer_id
        customer = self.get_from_id(customer_id, self.customers)
        result += str(customer) + "\n"
        trainer_id = subscription.trainer_id
        trainer = self.get_from_id(trainer_id, self.trainers)
        result += str(trainer) + "\n"
        exercise_id = subscription.exercise_id
        exercise = self.get_from_id(exercise_id, self.plans)
        equipment_id = exercise.equipment_id
        equipment = self.get_from_id(equipment_id, self.equipment)
        result += str(equipment) + "\n"
        result += str(exercise)
        return result
