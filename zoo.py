import json

class Zoo():

    DAILY_TIMES_EAT = 3
    DAYS_IN_MONTH = 30
    INCOME_PER_DAY_FOR_ANIMAL = 60
    FOODS_PRIZE = {"meat": 4, "others": 2, "foliage": 2, "grass": 2, "bamboo": 2}

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []
        self.animals_database = self._read_database("database.txt")

    def _check_equal_species_name(self, animal):
        for existing_animal in self.animals:
            if existing_animal.species == animal.species:
                if existing_animal.name == animal.name:
                    return True
        return False

    def add_animal(self, animal):
        there_is_place = len(self.animals) < self.capacity
        is_any_species = animal.species in self.animals_database
        theres_no_same_name = self._check_equal_species_name(animal) is False
        if there_is_place and is_any_species and theres_no_same_name:
            self.animals.append(animal)

    def _remove_dead_animal(self):
        new_animals_arr = []
        for animal in self.animals:
            if animal.is_dead is False:
                new_animals_arr.append(animal)
        self.animals = new_animals_arr

    def _read_database(self, file_name):
        with open(file_name, 'r') as file_content:
            file_data = json.load(file_content)
        return file_data

    def monthly_budget_update(self):
        for animal in self.animals:
            food_quality, food = animal.eat()
            food_cost = Zoo.FOODS_PRIZE[food]
            monthly_incomes = Zoo.INCOME_PER_DAY_FOR_ANIMAL * Zoo.DAYS_IN_MONTH
            eat_times_per_month = Zoo.DAILY_TIMES_EAT * Zoo.DAYS_IN_MONTH
            monthly_outcomes = food_quality * eat_times_per_month * food_cost
            self.budget += (monthly_incomes - monthly_outcomes)
            #maybe this method is FALSE!!!
