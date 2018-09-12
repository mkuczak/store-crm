import unittest
from src.manufacturer import Manufacturer
# NOTE: Test methods need to start with "test_" or else they won't be recognized.
# __init__(name, code, rules)


class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.a = Manufacturer("General Mills", "16000", ["First digit is a 1 for cereals and 2 for granola bars",
                                                         "Third digit is 3 for products conceived this decade, "
                                                         "2 for the last decade"])
        self.b = Manufacturer("Skippy", "37600", [])
        self.c = Manufacturer("Smucker's", "51500", ["First and second digits reserved for product lines."])
        self.d = Manufacturer("Cheetos", "28400", ["First, second, and third digits represents the variety",
                                                   "Fourth digit represents size package size",
                                                   "Fifth digit represents quantity of packages sold together"])

    def test_list_rules(self):
        self.assertEqual(self.a.list_rules(), "(1) First digit is a 1 for cereals and 2 for granola bars\n"
                                              "(2) Third digit is 3 for products conceived this decade, 2 for the last "
                                              "decade")
        self.assertEqual(self.b.list_rules(), "No rules have been set for this manufacturer.")
        self.assertEqual(self.c.list_rules(), "(1) First and second digits reserved for product lines.")

    def test_add_rule(self):
        self.b.add_rule("This is a new rule")
        self.assertEqual(self.b.rules, ["This is a new rule"])
        self.c.add_rule("Rules rule")
        self.assertEqual(self.c.rules, ["First and second digits reserved for product lines.", "Rules rule"])
        self.a.add_rule("Second digit depends on which state it was produced in", 2)
        self.assertEqual(self.a.rules, ["First digit is a 1 for cereals and 2 for granola bars",
                                        "Second digit depends on which state it was produced in",
                                        "Third digit is 3 for products conceived this decade, 2 for the last decade"])

    def test_remove_rule(self):
        with self.assertRaises(ValueError):
            self.a.remove_rule(0)
        with self.assertRaises(ValueError):
            self.a.remove_rule("I'm gonna input a string instead of an integer to try to break your program.")
        with self.assertRaises(IndexError):
            self.b.remove_rule(1)
        with self.assertRaises(IndexError):
            self.c.remove_rule(2)
        self.d.remove_rule(3)
        self.assertEqual(self.d.rules, ["First, second, and third digits represents the variety",
                                        "Fourth digit represents size package size"])

    def test_remove_all_rules(self):
        self.a.remove_all_rules()
        self.assertEqual(self.a.rules, [])


# Code below lets me test the code by running this py file.
if __name__ == '__main__':
    unittest.main
