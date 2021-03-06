import unittest

from TidyNumberGenerator import generate_greatest_tidy_number


class TestTidyNumberGenerator(unittest.TestCase):

    def test_case_general(self):
        self.assertEqual(generate_greatest_tidy_number("132"), 129)
        self.assertEqual(generate_greatest_tidy_number("+132"), 129)
        self.assertEqual(generate_greatest_tidy_number(" 132  "), 129)

    def test_long_edge_case(self):
        self.assertEqual(generate_greatest_tidy_number("1333333333333333333333333333333333333333333332"),
                         1299999999999999999999999999999999999999999999)

    def test_negative(self):
        with self.assertRaises(Exception):
            generate_greatest_tidy_number("-132")

    def test_value(self):
        with self.assertRaises(Exception):
            generate_greatest_tidy_number("-987a")

    def test_spaces_between_digits(self):
        with self.assertRaises(Exception):
            generate_greatest_tidy_number("1987 47")


if __name__ == '__main__':
    unittest.main()
