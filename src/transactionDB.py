from src.config import *
from src.transaction import *


def get_next_id():
    max_id = cursor.execute("SELECT MAX(ID) FROM Transactions").fetchone()
    if max_id is None:
        return 1
    else:
        return max_id + 1


def add_to_db(transaction):
    cart_string = ""
    for i in range(1,51):
        cart_string += ', :Cart_' + str(i)
    cursor.execute("INSERT INTO Items VALUES (:ID, :Payment_Method, :Card_Number, :Rewards_ID" + cart_string + ")",
                   {'ID': get_next_id(), 'Payment_Method': transaction.payment_method,
                    'Card_Number': transaction.card_number, 'Rewards_ID': transaction.rewards_id,
                    'Cart_1': transaction.cart[0], 'Cart_2': transaction.cart[1], 'Cart_3': transaction.cart[3],
                    'Cart_4': transaction.cart[3], 'Cart_5': transaction.cart[4], 'Cart_6': transaction.cart[5],
                    'Cart_7': transaction.cart[6], 'Cart_8': transaction.cart[7], 'Cart_9': transaction.cart[8],
                    'Cart_10': transaction.cart[9], 'Cart_11': transaction.cart[10], 'Cart_12': transaction.cart[11],
                    'Cart_13': transaction.cart[12], 'Cart_14': transaction.cart[13], 'Cart_15': transaction.cart[14],
                    'Cart_16': transaction.cart[15], 'Cart_17': transaction.cart[16], 'Cart_18': transaction.cart[17],
                    'Cart_19': transaction.cart[18], 'Cart_20': transaction.cart[19], 'Cart_21': transaction.cart[20],
                    'Cart_22': transaction.cart[21], 'Cart_23': transaction.cart[22], 'Cart_24': transaction.cart[23],
                    'Cart_25': transaction.cart[24], 'Cart_26': transaction.cart[25], 'Cart_27': transaction.cart[26],
                    'Cart_28': transaction.cart[27], 'Cart_29': transaction.cart[28], 'Cart_30': transaction.cart[29],
                    'Cart_31': transaction.cart[30], 'Cart_32': transaction.cart[31], 'Cart_33': transaction.cart[32],
                    'Cart_34': transaction.cart[33], 'Cart_35': transaction.cart[34], 'Cart_36': transaction.cart[35],
                    'Cart_37': transaction.cart[36], 'Cart_38': transaction.cart[37], 'Cart_39': transaction.cart[38],
                    'Cart_40': transaction.cart[39], 'Cart_41': transaction.cart[40], 'Cart_42': transaction.cart[41],
                    'Cart_43': transaction.cart[42], 'Cart_44': transaction.cart[43], 'Cart_45': transaction.cart[44],
                    'Cart_46': transaction.cart[45], 'Cart_47': transaction.cart[46], 'Cart_48': transaction.cart[47],
                    'Cart_49': transaction.cart[48], 'Cart_50': transaction.cart[49]})


def get_payment_method(tid):
    return cursor.execute("SELECT Payment_Method FROM Transactions WHERE ID=?", tid).fetchone()[0]


def get_card_number(tid):
    return cursor.execute("SELECT Card_Number FROM Transactions WHERE ID=?", tid).fetchone()[0]


def get_rewards_id(tid):
    return cursor.execute("SELECT Rewards_ID FROM Transactions WHERE ID=?", tid).fetchone()[0]


def get_cart(tid):
    cart = []
    row = cursor.execute("SELECT * FROM Transactions WHERE ID=?", tid).fetchone()
    for i in range(4,54):
        item = row[i]
        if item != "":
            cart.append(item)
    return cart


def extract_from_db(tid):
    return Transaction(get_cart(tid), get_payment_method(tid), get_card_number(tid), get_rewards_id(tid))


def remove_from_db(tid):
    cursor.execute("DELETE * FROM Transactions WHERE ID=?", tid)
