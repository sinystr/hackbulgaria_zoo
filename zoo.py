import database_helper
import config
import random
from animal import Animal


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

    def accommodate(self, species, age, name, gender, weight):
        animal = Animal(species, age, name, gender, weight)
        self.add_animal(animal)

    def _remove_dead_animal(self):
        new_animals_arr = []
        for animal in self.animals:
            if not animal.is_dead:
                new_animals_arr.append(animal)
        self.animals = new_animals_arr

    def move_to_habitat(self, species, name):
        new_animals_arr = []
        for animal in self.animals:
            if animal.species != species and animal.name != name:
                new_animals_arr.append(animal)
            elif animal.species == species and animal.name == name:
                print("The {}, {} is FREE!".format(animal.species, animal.name))
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

    def _generate_name(self):
        names_arr_len = len(config.NAMES)
        number = random.randrange(1, names_arr_len)
        return config.NAMES[number]

    def _generate_gender(self):
        number = random.randrange(1, 10)
        if number <= 5:
            return "male"
        else:
            return "female"

    def born_animal(self, mother):
        animal_info = self.animals_database[mother.species]
        baby_weight = animal_info["gender"]
        baby_name = self._generate_name()
        baby_species = mother.species
        baby_gender = self._generate_gender()
        new_animal = Animal(baby_species, 0, baby_name, baby_gender, baby_weight)
        self.add_animal(new_animal)
        return new_animal

    def _make_reproduction_moves(self):
        pass
