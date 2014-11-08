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
        self.species_info = animals_database[self.species]

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
        return 1, "meat"


"""
    def grow(self):



    def e
"""
