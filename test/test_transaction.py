import unittest
from src.transaction import Transaction
# NOTE: Test methods need to start with "test_" or else they won't be recognized.
# __init__(id, cart=None, payment_method=None, card_number=None, rewards_id=None)


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.g = Transaction(['016000275270', '051500006771', '051500006771', '051500006771'], 'credit',
                             '1000100010001000', 0)
        self.h = Transaction(['051500006771'], 'cash', 2)
        self.i = Transaction()

    # itemDB will have a method that tests barcode validity, so we do not need to do that here
    def test_add_to_cart(self):
        self.h.add_to_cart('016000275270')
        self.assertEqual(self.h.cart, ['051500006771', '016000275270'])
        self.i.add_to_cart('051500006771')
        self.assertEqual(self.i.cart, ['051500006771'])

    def test_remove_from_cart(self):
        self.g.remove_from_cart('2')
        self.assertEqual(self.g.cart, ['016000275270', '051500006771', '051500006771'])
        self.g.remove_from_cart('1')
        self.assertEqual(self.g.cart, ['051500006771', '051500006771'])
        with self.assertRaises(IndexError):
            self.h.remove_from_cart('2')
        with self.assertRaises(IndexError):
            self.i.remove_from_cart('1')
        with self.assertRaises(ValueError):
            self.g.remove_from_cart('0')
        with self.assertRaises(ValueError):
            self.g.remove_from_cart('5')

    def test_set_payment_method(self):
        with self.assertRaises(ValueError):
            self.i.set_payment_method("INVALID STRING")
        self.i.set_payment_method("credit")
        self.assertEqual(self.i.payment_method, "credit")
        self.i.set_payment_method("debit")
        self.assertEqual(self.i.payment_method, "debit")
        self.g.set_payment_method("credit")
        self.assertEqual(self.g.payment_method, "cash")
        self.h.set_payment_method("check")
        self.assertEqual(self.h.payment_method, "check")

    def test_set_card_number(self):
        with self.assertRaises(ValueError):
            self.i.set_card_number("0000")
        with self.assertRaises(ValueError):
            self.i.set_card_number("123456781234567K")
        self.g.set_card_number("1234567812345678")
        self.assertEqual(self.g.card_number, "1234567812345678")
        with self.assertRaises(AssertionError):
            self.h.set_card_number("1234567812345678")


if __name__ == '__main__':
    unittest.main
