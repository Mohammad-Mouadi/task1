import unittest
from BaseConversion import *


class TestBaseConversion(unittest.TestCase):

    def test_covert_to_decimal(self):
        self.assertEqual(BaseConversion.convert_to_decimal([15, 15], 16), 255)
        self.assertEqual(BaseConversion.convert_to_decimal([1, 0, 1, 0], 2), 10)
        self.assertEqual(BaseConversion.convert_to_decimal([1, 0, 1, 0], 10), 1010)

    def test_covert_from_decimal(self):
        self.assertEqual(BaseConversion.convert_from_decimal(255, 16), [15, 15])
        self.assertEqual(BaseConversion.convert_from_decimal(100, 10), [1, 0, 0])

    def test_covert_to_target(self):
        self.assertEqual(BaseConversion.convert([15], 16, 2), [1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
