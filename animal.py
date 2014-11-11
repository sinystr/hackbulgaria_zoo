import database_helper
import random
import config


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self._get_animal_stats()
        self.is_dead = False

    # Loads the common stats for the species
    def _get_animal_stats(self):
        animals_database = database_helper.read_database(config.DATABASE)
        if self.species in animals_database:
            self.species_info = animals_database[self.species]
        else:
            return False

    def _chance_of_dying(self):
        return self.age / self.species_info['life_expectancy']

    def try_die(self):
        if self.is_dead:
            # If the animal is dead it cannot die!
            return False
        if random.random() < self._chance_of_dying():
            self.is_dead = True
        return self.is_dead

    def eat(self):
        food_per_kg = self.species_info['food_weight_ratio']
        eaten_food = self.weight * food_per_kg
        food_cost = config.FOODS_PRIZE[self.species_info['food_type']]
        cost = eaten_food * food_cost
        return int(cost)

    def grow(self, months):
        self.age += months
        adding_weight = self.species_info['weight_age_ration'] * months
        self.weight += adding_weight
