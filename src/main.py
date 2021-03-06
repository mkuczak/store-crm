from src.transaction.transaction_logic import new as transaction_new, search as transaction_search
from src.refund.refund_logic import new as refund_new, search as refund_search
from src.item.item_logic import new as item_new, search as item_search
from src.manufacturer.manufacturer_logic import new as manufacturer_new, search as manufacturer_search

from src.prompt import sep
import src.prompt as prompt


def main():
    sep()
    user_input = prompt.navigate_menu("Main Menu", "Transactions", "Refunds", "Items", "Manufacturers")
    sep()
    if user_input == 1:
        user_input = prompt.navigate_menu("Transactions", "New", "Search")
        sep()
        if user_input == 0:
            return
        elif user_input == 1:
            transaction_new()
            return
        elif user_input == 2:
            transaction_search()
            return
    elif user_input == 2:
        user_input = prompt.navigate_menu("Refunds", "New", "Search")
        sep()
        if user_input == 0:
            return
        elif user_input == 1:
            refund_new()
            return
        elif user_input == 2:
            refund_search()
            return
    elif user_input == 3:
        user_input = prompt.navigate_menu("Items", "New", "Search")
        sep()
        if user_input == 0:
            return
        elif user_input == 1:
            item_new()
            return
        elif user_input == 2:
            item_search()
            return
    elif user_input == 4:
        user_input = prompt.navigate_menu("Manufacturers", "New", "Search")
        sep()
        if user_input == 0:
            return
        elif user_input == 1:
            manufacturer_new()
            return
        elif user_input == 2:
            user_input = prompt.navigate_menu("Search Manufacturers", "By Name", "By Code")
            if user_input == 0:
                return
            elif user_input == 1:
                manufacturer_search(False)
            elif user_input == 2:
                manufacturer_search(True)
            return


while True:
    main()
