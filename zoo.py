import database_helper
import config


class Zoo():

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []
        self.animals_database = database_helper.read_database(config.DATABASE)

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
            if not animal.is_dead:
                new_animals_arr.append(animal)
        self.animals = new_animals_arr

    def _daily_budget_update(self):
        cost, income = 0, 0
        for animal in self.animals:
            cost += animal.eat() * config.DAILY_TIMES_EAT
            income += config.ANIMAL_INCOME_DAILY
        return income - cost

    def monthly_budget_update(self):
        day_budget = self._daily_budget_update()
        return day_budget * config.MONTH_DAYS

    def _update_zoo_budget(self, months):
        month_budget = self.monthly_budget_update()
        self.budget += months * month_budget

