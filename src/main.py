from src.transaction import Transaction
from src.refund import Refund
from src.item import Item
from src.manufacturer import Manufacturer

import src.transactionDB as transactionDB
import src.refundDB as refundDB
import src.itemDB as itemDB
import src.manufacturerDB as manufacturerDB

import src.prompt as prompt


def main():
    user_input = prompt.navigate_menu("Main Menu", "Transactions", "Refunds", "Items", "Manufacturers")
    sep()
    if user_input == 1:  # Transactions
        user_input = prompt.navigate_menu("Transactions", "New", "Search", "View All")
        sep()
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Transactions -> New
            pass
        elif user_input == 2:  # Transactions -> Search
            t_extraction = prompt.ff("Transaction -> Search", "ID", transactionDB.extract_from_db)
            sep()
            t_extraction[0].print_data(t_extraction[1])
            sep()
            return
        elif user_input == 3:  # Transactions -> View All
            pass
    elif user_input == 2:  # Refunds
        user_input = prompt.navigate_menu("Refunds", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Refunds -> New
            pass
        elif user_input == 2:  # Refunds -> Search
            extraction = prompt.ff("Refunds -> Search", "ID", refundDB.extract_from_db)
            sep()
            extraction.print_data()
            sep()
            return
        elif user_input == 3:  # Refunds -> View All
            pass
    elif user_input == 3:  # Items
        user_input = prompt.navigate_menu("Items", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Items -> New
            pass
        elif user_input == 2:  # Items -> Search
            extraction = prompt.ff("Items -> Search", "Barcode", itemDB.extract_from_db)
            sep()
            extraction.print_data()
            sep()
            return
        elif user_input == 3:  # Items -> View All
            pass
    elif user_input == 4:  # Manufacturers
        user_input = prompt.navigate_menu("Manufacturers", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Manufacturers -> New
            pass
        elif user_input == 2:  # Manufacturers -> Search
            extraction = prompt.ff("Manufacturers -> Search", "Name", manufacturerDB.extract_from_db_by_name)
            sep()
            extraction.print_data()
            sep()
            return
        elif user_input == 3:  # Manufacturers -> View All
            pass
    print("Invalid input.  Returning to the main menu.")


def sep():
    print("------------------------------")


while True:
    main()
