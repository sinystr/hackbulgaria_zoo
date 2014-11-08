import database_helper
import config


class Zoo():

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []
        self.animals_database = database_helper.read_database("database.txt")

    def _check_equal_species_name(self, animal):
        for existing_animal in self.animals:
            has_same_species = existing_animal.species == animal.species
            has_same_name = existing_animal.name == animal.name
            if has_same_name and has_same_species:
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

    def monthly_budget_update(self):
        for animal in self.animals:
            food_quality, food = animal.eat()
            food_cost = config.FOODS_PRIZE[food]
            monthly_incomes = config.ANIMAL_INCOME_DAILY * config.MONTH_DAYS
            eat_times_per_month = config.DAILY_TIMES_EAT * config.MONTH_DAYS
            monthly_outcomes = food_quality * eat_times_per_month * food_cost
            self.budget += (monthly_incomes - monthly_outcomes)
            #maybe this method is FALSE!!!
