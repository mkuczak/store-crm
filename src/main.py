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
    pass


# "Multiple Choice Prompt: Options are listed and the user only needs to select an int from the list.
def mc_prompt(heading, func, *choices):
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


# Free Form Prompt: User must input something (such as a barcode) with the heading being the only guidance.
def ff_prompt(heading, func):
    while True:
        print(heading)
        try:
            func(input("Input barcode: "))
            break
        except ValueError:
            print("ValueError: Try again.\n")
        except AssertionError:
            print("AssertionError: Try again.\n")


main()
