import database_helper


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

    def eat(self):
        return 1, "meat"


"""
    def grow(self):



    def e
"""
