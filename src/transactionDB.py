from src.config import *
from src.transaction import *


def get_next_id():
    max_id = cursor.execute("SELECT MAX(ID) FROM Transactions").fetchone()[0]
    if max_id is None:
        return 1
    else:
        return max_id + 1


def add_to_db(transaction):
    gap_cart = transaction.cart
    while len(gap_cart) < 50:
        gap_cart.append("")
    cart_string = ""
    for i in range(1, 51):
        cart_string += ', :Cart_' + str(i)
    cursor.execute("INSERT INTO Transactions VALUES (:ID, :Payment_Method, :Card_Number, :Rewards_ID" + cart_string +
                   ")", {'ID': get_next_id(), 'Payment_Method': transaction.payment_method,
                         'Card_Number': transaction.card_number, 'Rewards_ID': transaction.rewards_id,
                         'Cart_1': gap_cart[0], 'Cart_2': gap_cart[1], 'Cart_3': gap_cart[2],
                         'Cart_4': gap_cart[3], 'Cart_5': gap_cart[4], 'Cart_6': gap_cart[5],
                         'Cart_7': gap_cart[6], 'Cart_8': gap_cart[7], 'Cart_9': gap_cart[8],
                         'Cart_10': gap_cart[9], 'Cart_11': gap_cart[10], 'Cart_12': gap_cart[11],
                         'Cart_13': gap_cart[12], 'Cart_14': gap_cart[13], 'Cart_15': gap_cart[14],
                         'Cart_16': gap_cart[15], 'Cart_17': gap_cart[16], 'Cart_18': gap_cart[17],
                         'Cart_19': gap_cart[18], 'Cart_20': gap_cart[19], 'Cart_21': gap_cart[20],
                         'Cart_22': gap_cart[21], 'Cart_23': gap_cart[22], 'Cart_24': gap_cart[23],
                         'Cart_25': gap_cart[24], 'Cart_26': gap_cart[25], 'Cart_27': gap_cart[26],
                         'Cart_28': gap_cart[27], 'Cart_29': gap_cart[28], 'Cart_30': gap_cart[29],
                         'Cart_31': gap_cart[30], 'Cart_32': gap_cart[31], 'Cart_33': gap_cart[32],
                         'Cart_34': gap_cart[33], 'Cart_35': gap_cart[34], 'Cart_36': gap_cart[35],
                         'Cart_37': gap_cart[36], 'Cart_38': gap_cart[37], 'Cart_39': gap_cart[38],
                         'Cart_40': gap_cart[39], 'Cart_41': gap_cart[40], 'Cart_42': gap_cart[41],
                         'Cart_43': gap_cart[42], 'Cart_44': gap_cart[43], 'Cart_45': gap_cart[44],
                         'Cart_46': gap_cart[45], 'Cart_47': gap_cart[46], 'Cart_48': gap_cart[47],
                         'Cart_49': gap_cart[48], 'Cart_50': gap_cart[49]})
    connector.commit()


def get_payment_method(tid):
    try:
        return cursor.execute("SELECT Payment_Method FROM Transactions WHERE ID = ?", str(tid)).fetchone()[0]
    except TypeError:
        return None


def get_card_number(tid):
    try:
        return cursor.execute("SELECT Card_Number FROM Transactions WHERE ID = ?", str(tid)).fetchone()[0]
    except TypeError:
        return None


def get_rewards_id(tid):
    try:
        return cursor.execute("SELECT Rewards_ID FROM Transactions WHERE ID = ?", str(tid)).fetchone()[0]
    except TypeError:
        return None


def get_cart(tid):
    cart = []
    row = cursor.execute("SELECT * FROM Transactions WHERE ID = ?", str(tid)).fetchone()
    if row is None:
        return None
    for i in range(4, 54):
        item = row[i]
        if item != "":
            cart.append(item)
        else:
            break
    return cart


def extract_from_db(tid):
    if cursor.execute("SELECT * FROM Transactions WHERE ID = ?", str(tid)).fetchone() is None:
        raise ValueError
    return Transaction(get_cart(tid), get_payment_method(tid), get_card_number(tid), get_rewards_id(tid))


def remove_from_db(tid):
    if cursor.execute("SELECT * FROM Transactions WHERE ID = ?", str(tid)).fetchone() is None:
        raise ValueError
    cursor.execute("DELETE FROM Transactions WHERE ID=?", str(tid))
    connector.commit()
