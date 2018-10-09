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
            transaction_new()
            return
        elif user_input == 2:  # Transactions -> Search
            transaction_search()
            return
        elif user_input == 3:  # Transactions -> View All
            pass
    elif user_input == 2:  # Refunds
        user_input = prompt.navigate_menu("Refunds", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Refunds -> New
            refund_new()
            return
        elif user_input == 2:  # Refunds -> Search
            refund_search()
            return
        elif user_input == 3:  # Refunds -> View All
            pass
    elif user_input == 3:  # Items
        user_input = prompt.navigate_menu("Items", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Items -> New
            item_new()
            return
        elif user_input == 2:  # Items -> Search
            item_search()
            return
        elif user_input == 3:  # Items -> View All
            pass
    elif user_input == 4:  # Manufacturers
        user_input = prompt.navigate_menu("Manufacturers", "New", "Search", "View All")
        if user_input == 0:  # Main Menu
            return
        elif user_input == 1:  # Manufacturers -> New
            manufacturer_new()
            return
        elif user_input == 2:  # Manufacturers -> Search
            sep()
            user_input = prompt.navigate_menu("Search Manufacturers", "By Name", "By Code")
            if user_input == 0:  # Main Menu
                return
            elif user_input == 1:
                manufacturer_search(False)
            elif user_input == 2:
                manufacturer_search(True)
            return
        elif user_input == 3:  # Manufacturers -> View All
            pass
    print("Invalid input.  Returning to the main menu.")
    # Note this doesn't actually mean that the input was invalid while testing.  But the function should be built in
    # in such as way that you'll never touch this line unless you misplay


def transaction_new():
    _transaction = Transaction()
    while True:
        if prompt.ff("Scan items, or press enter to continue", "Barcode", _transaction.add_to_cart) is None:
            sep()
            n = prompt.mc("Options", options, "Continue", "Add items", "Remove items", "Cancel transaction")[1]
            sep()
            if n == 1:
                if len(_transaction.cart) > 0:
                    break
                else:
                    print("Error: No items in cart")
            elif n == 2:
                continue
            elif n == 3:
                if len(_transaction.cart) > 0:
                    _transaction.print_cart()
                    prompt.mc("Select item to remove", _transaction.remove_from_cart)
                else:
                    print("Error: No items in cart")
            elif n == 4:
                return
            else:
                print("Invalid input.")
        sep()
        print("Items scanned so far:")
        for _item in _transaction.cart:
            print(_item)
        n = 0
        while True:
            if prompt.mc("Select payment type", _transaction.set_payment_method, "cash", "credit", "debit") \
                    is None:
                n = prompt.mc("Options", options, "Select payment type", "Edit cart", "Cancel transaction")[1]
                if n == 1:
                    continue
                elif n == 2:
                    break
                elif n == 3:
                    return
        if n == 2:
            continue
        while True:
            if _transaction.payment_method != "cash":
                if prompt.ff("Input card number", "Card Number: ", _transaction.set_card_number) is None:
                    n = prompt.mc("Options", options, "Input card number", "Edit cart", "Cancel transaction")[1]
                    if n == 1:
                        continue
                    elif n == 2:
                        break
                    elif n == 3:
                        return
        if n == 2:
            continue
        # THIS IS WHERE THE RECEIPT IS PRINTED AND TRANSACTION ADDED TO DB, if you can get here.


def transaction_search():
    extraction = prompt.ff("Transaction -> Search", "ID", transactionDB.extract_from_db)
    sep()
    extraction[0].print_data(extraction[1])
    sep()


def refund_new():
    pass


def refund_search():
    extraction = prompt.ff("Refunds -> Search", "ID", refundDB.extract_from_db)
    sep()
    extraction.print_data()
    sep()


def item_new():
    sep()
    name = input("Input the name of this item: ")
    while True:
        sep()
        n = prompt.mc("Assign a manufacturer to the item", options, "Input by name", "Input by code", "Cancel item")[1]
        sep()
        if n == 1:
            m_info = prompt.ff("Manufacturer by name", "Name", manufacturerDB.get_code_from_name)
            if m_info is None:
                continue
            else:
                m_code = m_info[0]
                m_name = m_info[1]
                break
        elif n == 2:
            m_info = prompt.ff("Manufacturer by code", "Code", manufacturerDB.get_name_from_code)
            if m_info is None:
                continue
            else:
                m_name = m_info[0]
                m_code = m_info[1]
                break
        elif n == 3:
            return
    while True:
        sep()
        n = prompt.mc("Input the price of the item", options, "Input price", "Skip", "Cancel item")[1]
        if n == 1:
            try:
                price = input("Price: ")
                if price == "":
                    continue
                else:
                    price = float(price)
                    break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 2:
            price = float(0.00)
            break
        elif n == 3:
            return
    while True:
        sep()
        n = prompt.mc("Determine the rewards benefits of the item", options,
                      "No discount", "Input percent discount", "Input modified price", "Cancel item")[1]
        if n == 1:
            multiplier = float(1.00)
            break
        elif n == 2:
            try:
                percent = input("Percent off: ")
                multiplier = (100-float(percent))*0.01
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 3:
            try:
                modified_price = float(input("Modified price: "))
                multiplier = modified_price/price
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 4:
            return
    while True:
        sep()
        n = prompt.mc("Input the quantity of the item", options, "Input quantity", "Skip", "Cancel item")[1]
        if n == 1:
            try:
                quantity = int(input("Quantity: "))
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 2:
            quantity = 0
            break
        elif n == 3:
            return
    item = Item(m_name, name, price, multiplier, quantity)
    while True:
        i = 0
        sep()
        n = prompt.mc("Input the 5-digit code for this product", options, "Input code", "Auto-select", "Cancel item")[1]
        sep()
        if n == 1:
            p_code = input("Code: ")
            if p_code.isdigit() and len(p_code) == 5:
                try:
                    item.build_barcode('0', m_code, p_code)
                    break
                except ValueError:
                    print("An identical barcode already exists in the database.")
            else:
                print("Invalid input.")
                continue
        elif n == 2:
            while True:
                i += 1
                p_code = str(i)
                while len(p_code) < 5:
                    p_code = '0' + p_code
                try:
                    item.build_barcode('0', m_code, p_code)
                    break
                except ValueError:
                    continue
            break
        elif n == 3:
            return

    itemDB.add_to_db(item)
    print(name + " successfully added to the item database.")


def item_search():
    extraction = prompt.ff("Items -> Search", "Barcode", itemDB.extract_from_db)
    sep()
    extraction.print_data()
    sep()


def manufacturer_new():
    sep()
    while True:
        print("Input manufacturer name")
        name = input("Name: ")
        copy = manufacturerDB.get_code_from_name(name)
        if copy is None:
            break
        else:
            sep()
            print(name + " is being used by another manufacturer (code: " + copy + ")")
    sep()
    while True:
        print("Input 5-digit code")
        code = input("Code: ")
        if code.isdigit() and len(code) == 5:
            copy = manufacturerDB.get_name_from_code(code)
            if copy is None:
                break
            else:
                sep()
                print(copy + " is already using the code " + code)
        else:
            sep()
            print(code + " is an invalid 5-digit code")
    rules = []
    sep()
    while True:
        n = prompt.mc("Would you like to add product code rules to this manufacturer?", options, "Yes", "No",
                      "Cancel manufacturer")[1]
        if n == 1:
            my_rule = input("Rule " + str(len(rules) + 1) + ": ")
            rules.append(my_rule)
            sep()
            print("Current rules: ")
            for rule in rules:
                print(rule)
        elif n == 2:
            break
        elif n == 3:
            sep()
            return
        else:
            sep()
            print("Invalid input")
    manufacturerDB.add_to_db(Manufacturer(name, code, rules))
    print(name + " successfully added to the manufacturer database.")
    sep()


def manufacturer_search(code):
    if code is False:
        extraction = prompt.ff("Manufacturers -> Search", "Name", manufacturerDB.extract_from_db_by_name)[0]
    else:
        extraction = prompt.ff("Manufacturers -> Search", "Code", manufacturerDB.extract_from_db_by_code)[0]
    sep()
    extraction.print_data()
    sep()


def sep():
    print("------------------------------")


def options(n):
    return n


while True:
    main()
