from animal import Animal
from zoo import Zoo
import unittest
import config


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
        ivan_pantera = Animal("pantera", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(ivan_pantera)
        self.assertEqual(len(self.zoopark.animals), 1)

    def test_check_equal_species_name_false(self):
        ivan_tiger = Animal("tiger", 4, "Ivan", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.assertFalse(self.zoopark._check_equal_species_name(gosho_tiger))

    def test_check_equal_species_name_true(self):
        ivan_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.assertTrue(self.zoopark._check_equal_species_name(gosho_tiger))

    def test_daily_budget_upd(self):
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.add_animal(gosho_tiger)
        self.assertEqual(self.zoopark._daily_budget_update(), 24)

    def test_daily_budget_upd_no_animals(self):
        self.assertEqual(self.zoopark._daily_budget_update(), 0)

    def test_monthly_budget_upd(self):
        ivan_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        self.assertEqual(self.zoopark.monthly_budget_update(), 744)

    def test_zoo_budget_update(self):
        ivan_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(ivan_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark._update_zoo_budget(2)
        self.assertEqual(self.zoopark.budget, 2981)

    def test_generate_name(self):
        name = self.zoopark._generate_name()
        self.assertIn(name, config.NAMES)

    def test_generate_gender(self):
        gender = self.zoopark._generate_gender()
        self.assertIn(gender, ["male", "female"])

    def test_born_baby(self):
        yana_tiger = Animal("tiger", 7, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        baby = self.zoopark.born_animal(yana_tiger)
        self.assertEqual(len(self.zoopark.animals), 2)
        self.assertEqual(baby.species, "tiger")
        self.assertEqual(baby.age, 0)
        self.assertIn(baby.name, config.NAMES)
        self.assertIn(baby.gender, ["male", "female"])
        self.assertEqual(baby.weight, 10)

    def test_accommodate(self):
        new_zoo = Zoo(1, 5)
        new_zoo.accommodate("tiger", 6, "misho", "male", 20)
        self.assertEqual(len(new_zoo.animals), 1)

    def test_accommodate_no_same_species(self):
        new_zoo = Zoo(1, 5)
        new_zoo.accommodate("pantera", 6, "misho", "male", 20)
        self.assertEqual(len(new_zoo.animals), 0)

    def test_move_to_habitat(self):
        self.zoopark.add_animal(self.puh_panda)
        self.zoopark.move_to_habitat("panda", "Puh")
        self.assertEqual(len(self.zoopark.animals), 0)

    def test_give_me_female_one(self):
        self.zoopark.add_animal(self.puh_panda)
        yana_tiger = Animal("tiger", 4, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        female = self.zoopark._give_me_female_one(self.puh_panda, yana_tiger)
        self.assertEqual(female.name, "Yana")

    def test_pregnance_reqs_female_true(self):
        yana_tiger = Animal("tiger", 7, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        self.assertTrue(self.zoopark._pregnance_reqs_female(yana_tiger))

    def test_pregnance_reqs_female_false1(self):
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        self.assertFalse(self.zoopark._pregnance_reqs_female(yana_tiger))

    def test_pregnance_reqs_female_false2(self):
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        yana_tiger.is_pregnant = True
        self.zoopark.animals.append(yana_tiger)
        self.assertFalse(self.zoopark._pregnance_reqs_female(yana_tiger))

    def test_make_reproduction_moves_true_one_couple(self):
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.make_reproduction_moves()
        self.assertTrue(yana_tiger.is_pregnant)
        self.assertEqual(yana_tiger.gestination_period, 0)

    def test_make_reproduction_moves_true_some_animals(self):
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.animals.append(self.puh_panda)
        puha_panda_f = Animal("panda", 8, "Vanya", "female", 100)
        self.zoopark.animals.append(puha_panda_f)
        dif_animal = Animal("bear", 8, "Vasilka", "female", 100)
        self.zoopark.animals.append(dif_animal)
        self.zoopark.make_reproduction_moves()
        self.assertTrue(yana_tiger.is_pregnant)
        self.assertEqual(yana_tiger.gestination_period, 0)
        self.assertTrue(puha_panda_f.is_pregnant)
        self.assertEqual(puha_panda_f.gestination_period, 0)

    def test_make_reproduction_moves_false1_one_couple(self):
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.make_reproduction_moves()
        self.assertFalse(yana_tiger.is_pregnant)

    def test_make_reproduction_moves_false2_one_couple(self):
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        yana_tiger.is_pregnant = True
        yana_tiger.gestination_period = 4
        self.zoopark.animals.append(yana_tiger)
        gosho_tiger = Animal("tiger", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.make_reproduction_moves()
        self.assertEqual(yana_tiger.gestination_period, 4)

    def test_make_reproduction_moves_false3_one_couple(self):
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        gosho_tiger = Animal("panda", 4, "Gosho", "male", 30)
        self.zoopark.animals.append(gosho_tiger)
        self.zoopark.make_reproduction_moves()
        self.assertFalse(yana_tiger.is_pregnant)

    def test_make_reproduction_moves_false4(self):
        yana_tiger = Animal("tiger", 5, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        self.zoopark.make_reproduction_moves()
        self.assertFalse(yana_tiger.is_pregnant)

    def test_actions_with_pregnant_one(self):
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        yana_tiger.is_pregnant = True
        self.zoopark.animals.append(yana_tiger)
        self.zoopark.actions_with_pregnant_one(5)
        self.assertEqual(yana_tiger.gestination_period, 5)
        self.assertEqual(len(self.zoopark.animals), 1)
        self.assertEqual(yana_tiger.relax_period, 8)

    def test_actions_with_pregnant_one_new_baby(self):
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        yana_tiger.is_pregnant = True
        self.zoopark.animals.append(yana_tiger)
        self.zoopark.actions_with_pregnant_one(8)
        self.assertEqual(yana_tiger.gestination_period, 0)
        self.assertEqual(len(self.zoopark.animals), 2)
        self.assertEqual(yana_tiger.relax_period, 2)
        baby = self.zoopark.animals[1]
        self.assertEqual(baby.age, 2)

    def test_growing(self):
        self.zoopark.animals.append(self.puh_panda)
        yana_tiger = Animal("tiger", 8, "Yana", "female", 30)
        self.zoopark.animals.append(yana_tiger)
        self.zoopark.grow_animals(5)
        self.assertEqual(self.puh_panda.age, 8)
        self.assertEqual(yana_tiger.age, 13)

if __name__ == '__main__':
    unittest.main()
