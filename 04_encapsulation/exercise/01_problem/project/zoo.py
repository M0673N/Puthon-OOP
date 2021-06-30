from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animals_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animals_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {str(type(animal)).split('.')[2][:-2]} added to the zoo"
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {str(type(worker)).split('.')[2][:-2]} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = []
        for worker in self.workers:
            salaries.append(worker.salary)
        total_cost = sum(salaries)
        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        cost = []
        for animal in self.animals:
            cost.append(animal.get_needs())
        total_cost = sum(cost)
        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        new_line = "\n"
        lions_list = [str(lion) for lion in self.animals if type(lion) == Lion]
        tigers_list = [str(tiger) for tiger in self.animals if type(tiger) == Tiger]
        cheetahs_list = [str(cheetah) for cheetah in self.animals if type(cheetah) == Cheetah]
        result = f"You have {len(self.animals)} animals\n" \
                 f"----- {len(lions_list)} Lions:\n" \
                 f"{new_line.join(lions_list)}\n" \
                 f"----- {len(tigers_list)} Tigers:\n" \
                 f"{new_line.join(tigers_list)}\n" \
                 f"----- {len(cheetahs_list)} Cheetahs:\n" \
                 f"{new_line.join(cheetahs_list)}"

        return result

    def workers_status(self):
        new_line = "\n"
        caretakers_list = [str(caretaker) for caretaker in self.workers if type(caretaker) == Caretaker]
        keepers_list = [str(keeper) for keeper in self.workers if type(keeper) == Keeper]
        vets_list = [str(vet) for vet in self.workers if type(vet) == Vet]
        result = f"You have {len(self.workers)} workers\n" \
                 f"----- {len(keepers_list)} Keepers:\n" \
                 f"{new_line.join(keepers_list)}\n" \
                 f"----- {len(caretakers_list)} Caretakers:\n" \
                 f"{new_line.join(caretakers_list)}\n" \
                 f"----- {len(vets_list)} Vets:\n" \
                 f"{new_line.join(vets_list)}"

        return result
