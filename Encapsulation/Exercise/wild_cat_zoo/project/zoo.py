class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):

        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:

            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):

        if len(self.workers) == self.__workers_capacity:

            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):

        for worker in self.workers:

            if worker.name == worker_name:

                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):

        workers_salary_sum = sum(w.salary for w in self.workers)

        if self.__budget >= workers_salary_sum:

            self.__budget -= workers_salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        animals_total_money_for_care = sum(a.money_for_care for a in self.animals)

        if self.__budget >= animals_total_money_for_care:

            self.__budget -= animals_total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):

        self.__budget += amount

    def animals_status(self):

        # result = f'You have {len(self.animals)} animals\n'
        #
        # lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        # result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'
        #
        # tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        # result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'
        #
        # cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        # result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs) + '\n'
        #
        # return result

        lions = list(filter(lambda w: w.__class__.__name__ == 'Lion', self.animals))
        tigers = list(filter(lambda w: w.__class__.__name__ == 'Tiger', self.animals))
        cheetahs = list(filter(lambda w: w.__class__.__name__ == 'Cheetah', self.animals))

        result = [
            f"You have {len(self.animals)} animals\n"
            f"----- {len(lions)} Lions:"
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return '\n'.join(str(r) for r in result)

    def workers_status(self):

        # result = f'You have {len(self.workers)} workers\n'
        #
        # keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        # result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'
        #
        # caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        # result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'
        #
        # vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        # result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets) + '\n'
        #
        # return result

        info = {"Caretaker": [], "Vet": [], "Keeper": []}
        [info[x.__class__.__name__].append(str(x)) for x in self.workers]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(info['Keeper'])} Keepers:",
            *info['Keeper'],
            f"----- {len(info['Caretaker'])} Caretakers:",
            *info['Caretaker'],
            f"----- {len(info['Vet'])} Vets:",
            *info['Vet']
        ]

        return '\n'.join(result)