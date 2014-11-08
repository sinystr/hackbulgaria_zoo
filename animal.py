import database_helper
import random


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self._get_animal_stats()

    # Loads the common stats for the species
    def _get_animal_stats(self):
        animals_database = database_helper.read_database("database.txt")
        self.species_info = animals_database[self.species]

    def _chance_of_dying(self):
        return self.age / self.species_info['life_expectancy']

    def try_die(self):
        return random.random() < self._chance_of_dying()

    def eat(self):
        return 1, "meat"


"""
    def grow(self):



    def e
"""
