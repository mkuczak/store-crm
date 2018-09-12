import unittest
from src.manufacturer import *
import src.manufacturerDB as mDB
from tests.db_setup import *
# NOTE: Test methods need to start with "test_" or else they won't be recognized.
# NOTE: These tests need to be taken with a grain of salt.  Usually, unit tests shouldn't depend on each other to work.
#       However, it's difficult to do this when you are inputting and extracting data from a database.
#       I tested this more manually by using DB Browser for SQLite: https://github.com/sqlitebrowser/sqlitebrowser


class TestManufacturerDB(unittest.TestCase):

    def setUp(self):
        self.z = Manufacturer("Nutella", "09800", ["This is the first rule", "This is the second rule",
                                                   "This is the third and final rule"])

    def test_add_to_db(self):
        mDB.add_to_db(self.z)
        table_as_list = t_cursor.execute("SELECT * FROM Manufacturers").fetchall()
        self.assertEqual(len(table_as_list), 3)
        self.assertEqual(table_as_list[2], ("Nutella", "09800", "This is the first rule", "This is the second rule",
                                            "This is the third and final rule"))

    def test_remove_from_db_by_name(self):
        table_as_list = t_cursor.execute("SELECT * FROM Manufacturers").fetchall()
        self.assertEqual(len(table_as_list), 3)
        mDB.remove_from_db_by_name("Nutella")
        table_as_list = t_cursor.execute("SELECT * FROM Manufacturers").fetchall()
        self.assertEqual(len(table_as_list), 2)
        # The next test will fail if test_get_code_from_name(self) doesn't pass.  Comment out in that case.
        self.assertEqual(mDB.get_code_from_name("Nutella"), None)

    # Skipping test_remove_from_db_by_name(self) due to redundancy.

    def test_get_name_from_code(self):
        self.assertEqual(mDB.get_name_from_code('16000'), "General Mills")
        self.assertEqual(mDB.get_name_from_code('51500'), "Smucker's")

    def test_get_code_from_name(self):
        self.assertEqual(mDB.get_code_from_name("General Mills"), '16000')
        self.assertEqual(mDB.get_code_from_name("Smucker's"), '51500')

    def test_get_rules_from_name(self):
        self.assertEqual(mDB.get_rules_from_name("General Mills"), ['Do not pick up the phone', 'Do not let him in'])
        self.assertEqual(mDB.get_rules_from_name("Smuckers"), ['Do not be his friend',
                                                               'You know that you will be waking up in his bed in the '
                                                               'morning', 'If you are under him'])

    def test_get_rules_from_code(self):
        self.assertEqual(mDB.get_rules_from_name('16000'), ['Do not pick up the phone', 'Do not let him in'])
        self.assertEqual(mDB.get_rules_from_name('51500'), ['Do not be his friend',
                                                            'You know that you will be waking up in his bed in the '
                                                            'morning', 'If you are under him'])


# Code below lets me test the code by running this py file.
if __name__ == '__main__':
    unittest.main
