from animal import Animal
import unittest


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.puh_panda = Animal("panda", 20, "Puh", "male", 100)

    def test_init_animal(self):
        self.assertEqual(self.puh_panda.species, "panda")
        self.assertEqual(self.puh_panda.age, 20)
        self.assertEqual(self.puh_panda.name, "Puh")
        self.assertEqual(self.puh_panda.gender, "male")
        self.assertEqual(self.puh_panda.weight, 100)

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

    def test_try_cannot_die_twice(self):
        results = []
        life_expectancy = self.puh_panda.species_info['life_expectancy']
        # making sure the chance is average
        self.puh_panda.age = life_expectancy // 2
        for i in range(0, 100):
            results.append(self.puh_panda.try_die())

        self.assertEqual(results.count(True), 1)

    def test_eat(self):
        self.assertEqual(self.puh_panda.eat(), 60)

    def test_grow(self):
        self.puh_panda.grow(5)
        self.assertEqual(self.puh_panda.age, 25)
        self.assertEqual(self.puh_panda.weight, 101.5)
        self.assertEqual(self.puh_panda.relax_period, 25)
        self.assertEqual(self.puh_panda.gestination_period, 0)
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        yana_tiger.is_pregnant = True
        yana_tiger.grow(5)
        self.assertEqual(yana_tiger.relax_period, 0)
        ivo_tiger = Animal("tiger", 5, "Ivo", "female", 101)
        ivo_tiger.grow(5)
        #cannot get bigger anymore, it is fat enough
        self.assertEqual(ivo_tiger.weight, 101)

    def test_get_pregnant(self):
        self.puh_panda.get_pregnant()
        self.assertTrue(self.puh_panda.is_pregnant)
        self.assertEqual(self.puh_panda.gestination_period, 0)
        self.assertEqual(self.puh_panda.relax_period, 0)

if __name__ == '__main__':
    unittest.main()
