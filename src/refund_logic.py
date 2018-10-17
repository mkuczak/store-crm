from src.transaction import Transaction  # Try removing this and see if it breaks
from src.refund import Refund

import src.transactionDB as transactionDB
import src.refundDB as refundDB

from src.prompt import sep, options
import src.prompt as prompt


def new():
    sep()
    try:
        extraction = prompt.ff("Input the transaction ID for which to process a refund", "Transaction ID",
                               transactionDB.extract_from_db)
    except ValueError:
        sep()
        print("Invalid ID.  Returning to menu.")
        sep()
        return
    t_id = extraction[1]
    transaction = extraction[0]
    refund = Refund(t_id)
    print("The following items are associated with the transaction ID " + t_id + ":")
    transaction.print_cart()
    while True:
        if len(refund.items) > 0:
            print("Items to be refunded: ")
            refund.print_items()
        if prompt.ff("Scan item to be returned, or press enter for more options", "Barcode", refund.add_to_items,
                     transaction.cart) is None:
            sep()
            n = prompt.mc("Options", options,
                          "Continue", "Return all items", "Add items", "Remove items", "Cancel transaction")[1]
            if n == 1:
                if len(refund.items) > 0:
                    break
                else:
                    print("Error: No items in refund list")
            elif n == 2:
                refund.add_all_to_items(transaction.cart)
                break
            elif n == 3:
                continue
            elif n == 4:
                if len(refund.items) > 0:
                    refund.print_items()
                    prompt.mc("Select item to remove", refund.remove_from_items)
                else:
                    print("Error: No items in refund list.")
            elif n == 5:
                sep()
                return
    sep()
    refund.reason = prompt.ff("What is the reason for returning these items?", "Reason", options)[1]
    sep()
    refundDB.add_to_db(refund)
    print("Refund successfully processed.")
    sep()


def search():
    extraction = prompt.ff("Refunds -> Search", "ID", refundDB.extract_from_db)
    sep()
    extraction.print_data()
    sep()
