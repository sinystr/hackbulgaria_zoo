import unittest
from interface import make_months, split_command_str, the_command


class Interface_test(unittest.TestCase):

    def test_split_command_str(self):
        array = split_command_str("I am Mihail")
        self.assertEqual(array[0], "I")
        self.assertEqual(array[1], "am")
        self.assertEqual(array[2], "Mihail")

    def test_the_command(self):
        array = split_command_str("I am Mihail")
        self.assertTrue(the_command(array, "I"))
        self.assertFalse(the_command(array, "am"))

    def test_make_months_days(self):
        months = make_months(15.5, "days")
        self.assertEqual(months, 0.5)

    def test_make_months_months(self):
        months = make_months(15.5, "months")
        self.assertEqual(months, 15.5)

    def test_make_months_weeks(self):
        months = make_months(2, "weeks")
        self.assertEqual(months, 0.45248868778280543)

    def test_make_months_years(self):
        months = make_months(2, "years")
        self.assertEqual(months, 24)

if __name__ == '__main__':
    unittest.main()
