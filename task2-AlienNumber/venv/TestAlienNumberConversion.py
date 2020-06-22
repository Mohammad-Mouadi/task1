import unittest

from AlienNumbersConversion import AlienNumbersConversion


class TestAlienNumberConversion(unittest.TestCase):
    def test_case_general(self):
        self.assertEqual(AlienNumbersConversion.covert_alien_number_to_target_language("9", "0123456789", "oF8"), "Foo")
        self.assertEqual(AlienNumbersConversion.covert_alien_number_to_target_language("CODE", "O!CDE?", "A?JM!."),
                         "JAM!")
        self.assertEqual(AlienNumbersConversion.covert_alien_number_to_target_language("ff", "0123456789abcdef", "01"),
                         "11111111")


if __name__ == '__main__':
    unittest.main()
