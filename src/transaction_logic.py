from src.transaction import Transaction

import src.transactionDB as transactionDB

from src.prompt import sep, options
import src.prompt as prompt


def new():
    _transaction = Transaction()
    while True:
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
            break
        if n == 2:
            continue
        while True:
            if _transaction.payment_method != "cash":
                sep()
                if prompt.ff(_transaction.payment_method[0].upper() + _transaction.payment_method[1:] + " selected",
                             "Card Number", _transaction.set_card_number) is None:
                    n = prompt.mc("Options", options, "Input card number", "Edit cart", "Cancel transaction")[1]
                    if n == 1:
                        continue
                    elif n == 2:
                        break
                    elif n == 3:
                        return
                break
            break
        if n == 2:
            continue
        sep()
        transactionDB.add_to_db(_transaction)
        print("Transaction added")
        # THIS IS WHERE THE RECEIPT IS PRINTED AND TRANSACTION ADDED TO DB, if you can get here.
        break
    sep()


def search():
    extraction = prompt.ff("Transaction -> Search", "ID", transactionDB.extract_from_db)
    sep()
    extraction[0].print_data(extraction[1])
    sep()
