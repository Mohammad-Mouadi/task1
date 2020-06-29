import unittest

from AlienNumbersConverter import AlienNumbersConverter


class TestAlienNumberConverter(unittest.TestCase):

    def test_case_general(self):
        self.assertEqual(AlienNumbersConverter.convert(AlienNumbersConverter("9 0123456789 oF8")), "Foo")

    def test_case_valid_input(self):
        with self.assertRaises(TypeError):
            AlienNumbersConverter.convert(AlienNumbersConverter(None))

    def test_case_input_format(self):
        with self.assertRaises(Exception):
            AlienNumbersConverter.convert(AlienNumbersConverter("90123456789 oF8"))

    def test_case_valid_num(self):
        with self.assertRaises(Exception):
            AlienNumbersConverter.convert(AlienNumbersConverter("9a 0123456789 oF8"))

    def test_case_valid_source_digits(self):
        with self.assertRaises(Exception):
            AlienNumbersConverter.convert(AlienNumbersConverter("9 01234456789 oF8"))

    def test_case_valid_target_digits(self):
        with self.assertRaises(Exception):
            AlienNumbersConverter.convert(AlienNumbersConverter("9 01234456789 oFF8"))


if __name__ == '__main__':
    unittest.main()
