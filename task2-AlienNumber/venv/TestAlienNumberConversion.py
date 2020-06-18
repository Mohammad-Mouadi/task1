import unittest

from AlienNumbersConversion import AlienNumbersConversion
class TestAlienNumberConversion(unittest.TestCase):
    def test_case_general(self):
        self.assertEqual(AlienNumbersConversion.covert_alien_number_to_source_language("9","0123456789","oF8"), "Foo")


if __name__ == '__main__':
    unittest.main()
