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
                print("The {}, {} is FREE!".format(animal.species,
                                                   animal.name))
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
        baby_weight = animal_info["newborn_weight"]
        baby_name = self._generate_name()
        baby_species = mother.species
        baby_gender = self._generate_gender()
        new_animal = Animal(baby_species, 0,
                            baby_name, baby_gender, baby_weight)
        self.add_animal(new_animal)
        return new_animal

    def _give_me_female_one(self, animal1, animal2):
        if animal1.gender == "female":
            return animal1
        else:
            return animal2

    def _pregnance_reqs_female(self, animal):
        if animal.is_pregnant is False:
            if animal.relax_period >= config.RELAX_PERIOD:
                return True
        return False

    def make_reproduction_moves(self):
        for animal1 in self.animals:
            for animal2 in self.animals:
                equal_species = animal1.species == animal2.species
                different_genders = animal1.gender != animal2.gender
                if equal_species and different_genders:
                    female_one = self._give_me_female_one(animal1, animal2)
                    if self._pregnance_reqs_female(female_one) is True:
                        female_one.get_pregnant()
                        print("A {} will be born".format(female_one.species))

    def actions_with_pregnant_one(self, months):
        for animal in self.animals:
            is_female = animal.gender == "female"
            is_pregnant = animal.is_pregnant is True
            if is_female and is_pregnant:
                animal.gestination_period += months
                for_the_species = self.animals_database[animal.species]
                species_gest_period = int(for_the_species["gestation_period"])
                if animal.gestination_period >= species_gest_period:
                    baby = self.born_animal(animal)
                    difference = animal.gestination_period - species_gest_period
                    baby.age += difference
                    animal.relax_period = difference
                    animal.gestination_period = 0
                    print("The {} {} is born and it is {} months old".format(
                                            baby.species, baby.name, baby.age))

    def print_dead_animals(self):
        for animal in self.animals:
            animal.try_die()
            if animal.is_dead:
                print("{} the {} is dead :(".format(animal.name,
                                                    animal.species))

    def grow_animals(self, months):
        for animal in self.animals:
            animal.grow(months)

    def can_feed_animals(self, months):
        if self.budget > 0:
            return True
        return False
