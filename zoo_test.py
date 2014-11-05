from zoo import Zoo
import unittest


class Zoo_test(unittest.TestCase):

    def setUp(self):
        self.zoopark = Zoo(10, 5)

    def test_init_animal(self):
        self.assertEqual(self.zoopark.capacity, 10)
        self.assertEqual(self.zoopark.budget, 5)


if __name__ == '__main__':
    unittest.main()
