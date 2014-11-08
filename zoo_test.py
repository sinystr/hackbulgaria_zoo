from animal import Animal
from zoo import Zoo
import unittest


class Zoo_test(unittest.TestCase):

    def setUp(self):
        self.zoopark = Zoo(2, 5)
        self.puh_panda = Animal("panda", 3, "Puh", "male", 100)

    def test_init_animal(self):
        self.zoopark.animals.append(self.puh_panda)
        self.assertEqual(self.zoopark.capacity, 2)
        self.assertEqual(self.zoopark.budget, 5)
        self.assertEqual(self.zoopark.animals[0], self.puh_panda)

    def test_add_animal(self):
        self.zoopark.add_animal(self.puh_panda)
        self.assertEqual(self.zoopark.animals[0], self.puh_panda)
        self.assertEqual(len(self.zoopark.animals), 1)

    def test_add_animal_full_zoo(self):
        self.zoopark.add_animal(self.puh_panda)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(gosho_tiger)
        ivan_tiger = Animal("tiger", 4, "Ivan", "male", 30)
        self.zoopark.add_animal(ivan_tiger)
        self.assertEqual(len(self.zoopark.animals), 2)
        self.assertEqual(self.zoopark.animals[0], self.puh_panda)
        self.assertEqual(self.zoopark.animals[1], gosho_tiger)

    def test_add_animal_same_name(self):
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(gosho_tiger)
        ivan_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(ivan_tiger)
        self.assertEqual(len(self.zoopark.animals), 1)
        self.assertEqual(self.zoopark.animals[0], gosho_tiger)

    def test_add_no_same_species(self):
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(gosho_tiger)
        ivan_elephant = Animal("elephant", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(ivan_elephant)
        self.assertEqual(len(self.zoopark.animals), 2)

    def test_check_equal_species_name_false(self):
        ivan_tiger = Animal("tiger", 4, "Ivan", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.assertFalse(self.zoopark._check_equal_species_name(gosho_tiger))

    def test_check_equal_species_name_true(self):
        ivan_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.assertTrue(self.zoopark._check_equal_species_name(gosho_tiger))

    def test_monthly_budget_update(self):
        self.zoopark.animals.append(self.puh_panda)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.monthly_budget_update()
        self.assertEqual(self.zoopark.budget, 2885)

    def test_monthly_budget_update_animal_dies(self):
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        ivan_tiger = Animal("tiger", 4, "Ivan", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.animals.append(self.puh_panda)
        self.zoopark.monthly_budget_update()
        self.zoopark.animals.remove(self.puh_panda)
        self.zoopark.animals.remove(gosho_tiger)
        self.zoopark.monthly_budget_update()
        self.assertEqual(self.zoopark.budget, 5765)


    #def test_check_for_dead_animal(self):


if __name__ == '__main__':
    unittest.main()
