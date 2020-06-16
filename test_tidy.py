import unittest

from tidy_number import greatest_tidy_number


class MyTestCase(unittest.TestCase):

    def test_short(self):
        self.assertEqual(greatest_tidy_number("132"), 129)

    def test_long(self):
        self.assertEqual(greatest_tidy_number("1333333333333333333333333333333333333333333332"),
                         1299999999999999999999999999999999999999999999)

    def test_negative(self):
        self.assertEqual(greatest_tidy_number("-132"), "Error: Negative number")

    def test_value(self):
        self.assertEqual(greatest_tidy_number("-987a"), "Invalid number")


if __name__ == '__main__':
    unittest.main()
