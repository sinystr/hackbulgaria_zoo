from animal import Animal
import unittest


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.puh_panda = Animal("panda", 20, "Puh", "male", 350)

    def test_init_animal(self):
        self.assertEqual(self.puh_panda.species, "panda")
        self.assertEqual(self.puh_panda.age, 20)
        self.assertEqual(self.puh_panda.name, "Puh")
        self.assertEqual(self.puh_panda.gender, "male")
        self.assertEqual(self.puh_panda.weight, 350)

    def test_chance_of_dying(self):
        chance = self.puh_panda._chance_of_dying()
        life_expectancy = self.puh_panda.species_info['life_expectancy']
        age = self.puh_panda.age
        self.assertEqual(chance, age / life_expectancy)

    def test_try_die(self):
        results = []
        life_expectancy = self.puh_panda.species_info['life_expectancy']
        # making sure the chance is average
        self.puh_panda.age = life_expectancy // 2

        for i in range(0, 100):
            results.append(self.puh_panda.try_die())

        self.assertTrue(False in results)
        self.assertTrue(True in results)

if __name__ == '__main__':
    unittest.main()
