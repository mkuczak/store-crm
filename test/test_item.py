import unittest
from src.item import Item
# NOTE: Test methods need to start with "test_" or else they won't be recognized.
# __init__(barcode, manufacturer, product, price, multiplier, quantity, barcode=None)


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.e = Item('', "General Mills", "Honey Nut Cheerios Cereal - 12oz", 3.99, 1.00, 90)  # 016000275270
        self.f = Item('', "Smucker's", "Smucker's: Cherry Preserves - 18oz", 4.55, 0.85, 0)  # 051500006771

    def test_build_barcode(self):
        self.e.build_barcode('0', '16000', '27527')
        assert(self.e.barcode == '016000275270')
        self.f.build_barcode('0', '51500', '00677')
        assert(self.f.barcode == '051500006771')


# Code below lets me test the code by running this py file.
if __name__ == '__main__':
    unittest.main
