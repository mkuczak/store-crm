import unittest
from transaction import Transaction
# NOTE: Test methods need to start with "test_" or else they won't be recognized.
# __init__(id, cart=None, payment_method=None, card_number=None, rewards_id=None)


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.g = Transaction(1, ['016000275270', '051500006771', '051500006771', '051500006771'], 'credit',
                             '1000-1000-1000-1000', 0)
        self.h = Transaction(['051500006771'], 'cash', 2)
        self.i = Transaction(3)

    # itemDB will have a method that tests barcode validity, so we do not need to do that here
    def test_add_to_cart(self):
        self.h.add_to_cart('016000275270')
        self.assertEqual(self.h.cart, ['051500006771', '016000275270'])
        self.i.add_to_cart('051500006771')
        self.assertEqual(self.i.cart, ['051500006771'])

    # itemDB will have a method that test for barcode validity, but remove_from_cart still need to check whether the
    # barcode was present in the cart before removal
    def test_remove_from_cart(self):
        self.g.remove_from_cart('051500006771')
        self.assertEqual(self.g.cart, ['016000275270', '051500006771', '051500006771'])
        self.g.remove_from_cart('016000275270')
        self.assertEqual(self.g.cart, ['051500006771', '051500006771'])
        with self.assertRaises(ValueError):
            self.h.remove_from_cart('016000275270')
        with self.assertRaises(ValueError):
            self.i.remove_from_cart('051500006771')

    def test_receipt(self):
        pass
        # MAke sure to come back for this one

if __name__ == '__main__':
    unittest.main