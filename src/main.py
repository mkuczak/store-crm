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
    src.config.cursor.execute("DELETE FROM Transactions")
    transactionDB.add_to_db(Transaction(['000011112222', '000022221111'], "credit", "1111111111111111", 3))
    transactionDB.add_to_db(Transaction(['000011112222', '000022221111'], "credit", "1111111111111111", 3))
    print("This should display 1111111111111111: " + transactionDB.get_card_number(1))
    print("This should display ['000011112222', '000022221111'] below: ")
    print(transactionDB.get_cart(1))
    print("This should display credit: " + transactionDB.get_payment_method(1))
    print("This should display 3: " + str(transactionDB.get_rewards_id(1)))
    print("This should display 1111111111111111: " + transactionDB.extract_from_db(1).card_number)
    transactionDB.remove_from_db(1)
    x = transactionDB.get_rewards_id(1)
    if x is None:
        print("Removal of transaction from DB SUCCESS.")
    else:
        print("Removal of transaction from DB FAILURE.")
    x = transactionDB.get_cart(1)
    if x is None:
        print("Removal of transaction from DB SUCCESS.")
    else:
        print("Removal of transaction from DB FAILURE.")
    try:
        transactionDB.remove_from_db(1)
        print("This message should have popped up if remove_from_db doesn't care about invalid tid")
    finally:
        print("If no message about remove_from_db exists above this, invalid tids don't throw errors.")


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
