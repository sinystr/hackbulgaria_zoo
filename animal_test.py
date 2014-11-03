from animal import Animal
import unittest


class Animal_test(unittest.TestCase):

    def setUp(self):
        self.puh_panda = Animal("panda", 36, "Puh", "male", 350)

    def test_init_animal(self):
        self.assertEqual(self.puh_panda.species, "panda")
        self.assertEqual(self.puh_panda.age, 36)
        self.assertEqual(self.puh_panda.name, "Puh")
        self.assertEqual(self.puh_panda.gender, "male")
        self.assertEqual(self.puh_panda.weight, 350)


if __name__ == '__main__':
    unittest.main()
