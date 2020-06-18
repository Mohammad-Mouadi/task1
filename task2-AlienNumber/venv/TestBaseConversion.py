import unittest
from BaseConversion import *

class TestBaseConversion(unittest.TestCase):
    def test(self):
        self.assertEqual(BaseConversion.convert_to_decimal([15,15],16), 255)
        self.assertEqual(BaseConversion.convert_from_decimal(255,16),[15,15])
        self.assertEqual(BaseConversion.convert([9],10,3),[1,0,0])


if __name__ == '__main__':
    unittest.main()
