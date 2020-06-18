import unittest

from .TidyNumberGenerator import *


class TestTidyNumberGenerator(unittest.TestCase):

    def test_short(self):
        self.assertEqual(generate_greatest_tidy("132"), 129)

    def test_long(self):
        self.assertEqual(generate_greatest_tidy("1333333333333333333333333333333333333333333332"),
                         1299999999999999999999999999999999999999999999)

    def test_negative(self):
        with self.assertRaises(Exception):
            generate_greatest_tidy("-132")

    def test_value(self):
        with self.assertRaises(Exception):
            generate_greatest_tidy("-987a")


if __name__ == '__main__':
    unittest.main()
