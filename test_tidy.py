import unittest

from tidy_number import greatest_tidy_number

class MyTestCase(unittest.TestCase):

    def test(self):
        self.assertEqual(greatest_tidy_number("132"), 129)


if __name__ == '__main__':
    unittest.main()
