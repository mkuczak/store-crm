from src.transaction import Transaction
from src.refund import Refund
from src.item import Item
from src.manufacturer import Manufacturer

import src.transactionDB as transactionDB
import src.refundDB as refundDB
import src.itemDB as itemDB
import src.manufacturer as manufacturerDB

import src.config


def main():
    src.config.cursor.execute("DELETE FROM Items")
    itemDB.add_to_db(Item("Manufacturer0", "Product0", 1.00, 0.85, 4, '022222111110'))
    itemDB.add_to_db(Item("Manufacturer1", "Product1", 0.89, 1.00, 9, '011111222220'))
    print("This should display 1.00: " + str(itemDB.get_price('022222111110')))
    print("This should display 0.85: " + str(itemDB.get_price('022222111110', True)))
    print("This should display 0.89: " + str(itemDB.get_price('011111222220', True)))
    print("This should display Manufacturer0 Product0: " + itemDB.get_name('022222111110'))
    print("This should display Product1: " + itemDB.get_name('011111222220', False))
    print("This should display 4: " + str(itemDB.get_quantity('022222111110')))
    itemDB.add_quantity('022222111110', 2)
    print("This should display 6: " + str(itemDB.get_quantity('022222111110')))
    print("This should display 9: " + str(itemDB.get_quantity('011111222220')))
    itemDB.subtract_quantity('011111222220', 7)
    print("This should display 2: " + str(itemDB.get_quantity('011111222220')))
    itemDB.set_product('022222111110', 'NewProduct0')
    print("This should display NewProduct0: " + str(itemDB.get_name('022222111110', False)))
    itemDB.set_price('022222111110', 2.00)
    print("This should display 2.00: " + str(itemDB.get_price('022222111110')))
    print("This should display 1.70: " + str(itemDB.get_price('022222111110', True)))
    itemDB.set_price('011111222220', 3)
    print("This should display 3.00: " + str(itemDB.get_price('011111222220')))

    itemDB.remove_from_db('022222111110')
    if itemDB.get_name('022222111110') is None:
        print("Item deletion SUCCESS")
    else:
        print("Item deletion FAILURE")

    try:
        itemDB.set_multiplier('022222111110', 0.10)
        print("Item deletion FAILURE")
    except ValueError:
        print("Item deletion SUCCESS")

    if itemDB.get_name('000000222220') is not None:
        print("Invalid barcode check FAILURE.")
    else:
        print("Invalid barcode check SUCCESS.")
    print("This should display 011111222220: " + itemDB.extract_from_db('011111222220').barcode)


def numbered_prompt(heading, func, *choices):
    while True:
        print(heading)
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        try:
            func(int(input("Input value: ")))
            break
        except ValueError:
            print("ValueError: Try again.\n")
        except IndexError:
            print("IndexError: Try again.\n")
        except AssertionError:
            print("AssertionError: Try again.\n")


main()
