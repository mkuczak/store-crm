import unittest
from src.refund.refund import Refund
from src.transaction.transaction import Transaction
# NOTE: Test methods need to start with "test_" or else they won't be recognized.


class TestRefund(unittest.TestCase):

    def setUp(self):

        self.i = Refund(1, ['051500006771'], 'Accidental purchase')
        self.j = Refund(2, ['016000275270', '016000275270'])
        self.k = Refund(3, ['016000275270', '016000275270', '051500006771', '016000275270'], 'Expired')
        self.m = Refund(4)
        self.n = Refund(5)

        self.g = Transaction(['016000275270', '051500006771', '051500006771', '051500006771'], 'credit',
                             '1000100010001000', 0)
        self.h = Transaction(['051500006771'], 'cash', 2)

    # transaction will be recreated as an object using transactionDB and used as an input param for add_to_items
    def test_add_to_items(self):

        with self.assertRaises(ValueError):
            self.m.add_to_items('016000275270', self.h.cart)
        with self.assertRaises(ValueError):
            self.m.add_to_items('111111111111', self.h.cart)
        self.m.add_to_items('051500006771', self.h.cart)
        self.assertEqual(self.m.items, ['051500006771'])

        self.i.add_to_items('051500006771', self.g.cart)
        self.assertEqual(self.i.items, ['051500006771', '051500006771'])

        self.n.add_to_items('016000275270', self.g.cart)
        self.assertEqual(self.n.items, ['016000275270'])
        with self.assertRaises(ValueError):
            self.n.add_to_items('016000275270', self.g.cart)
        self.assertEqual(self.n.items, ['016000275270'])
        self.n.add_to_items('051500006771', self.g.cart)
        self.assertEqual(self.n.items, ['016000275270', '051500006771'])
        self.n.add_to_items('051500006771', self.g.cart)
        self.assertEqual(self.n.items, ['016000275270', '051500006771', '051500006771'])
        self.n.add_to_items('051500006771', self.g.cart)
        self.assertEqual(self.n.items, ['016000275270', '051500006771', '051500006771', '051500006771'])
        with self.assertRaises(ValueError):
            self.n.add_to_items('051500006771', self.g.cart)
        self.assertEqual(self.n.items, self.g.cart)

    def test_add_all_to_items(self):
        self.m.add_all_to_items(self.g.cart)
        self.assertEqual(self.m.items, self.g.cart)
        self.n.add_all_to_items(self.h.cart)
        self.assertEqual(self.n.items, self.h.cart)

    def test_remove_from_items(self):
        with self.assertRaises(ValueError):
            self.i.remove_from_items('0')
        with self.assertRaises(ValueError):
            self.i.remove_from_items('-1')
        with self.assertRaises(ValueError):
            self.i.remove_from_items('Non-digit input')
        with self.assertRaises(IndexError):
            self.i.remove_from_items('2')
        self.assertEqual(self.i.items, ['051500006771'])
        self.i.remove_from_items(1)
        self.assertEqual(self.i.items, [])
        self.j.remove_from_items(1)
        self.assertEqual(self.j.items, ['016000275270'])


if __name__ == '__main__':
    unittest.main
