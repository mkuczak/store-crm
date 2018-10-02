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
    user_input = navigate_menu("Main Menu", "Transactions", "Refunds", "Items", "Manufacturers")
    if user_input == 1:  # Transactions
        user_input = navigate_menu("Transactions", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Transactions -> New
            pass
        elif user_input == 2:  # Transactions -> Search
            pass
        elif user_input == 3:  # Transactions -> View All
            pass
    elif user_input == 2:  # Refunds
        user_input = navigate_menu("Refunds", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Refunds -> New
            pass
        elif user_input == 2:  # Refunds -> Search
            pass
        elif user_input == 3:  # Refunds -> View All
            pass
    elif user_input == 3:  # Items
        user_input = navigate_menu("Items", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Items -> New
            pass
        elif user_input == 2:  # Items -> Search
            pass
        elif user_input == 3:  # Items -> View All
            pass
    elif user_input == 4:  # Manufacturers
        user_input = navigate_menu("Manufacturers", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Manufacturers -> New
            pass
        elif user_input == 2:  # Manufacturers -> Search
            pass
        elif user_input == 3:  # Manufacturers -> View All
            pass
    print("Invalid input.  Returning to the main menu.")


def navigate_menu(heading, *choices):
    while True:
        print("- " + heading + " -")
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        if heading != "Main Menu":
            print("0: Main Menu")
        try:
            decision = int(input("Input value: "))
            if 0 <= int(decision) <= n:
                return decision
        except ValueError:
            print("ValueError: Try again.\n")


# Multiple Choice Prompt: Options are listed and the user only needs to select an int from the list.
def mc_prompt(heading, func, *choices):
    while True:
        print(heading)
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        try:
            decision = int(input("Input value: "))
            func(decision)
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


while True:
    main()
