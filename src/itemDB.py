from src.config import *
from src.item import *


def add_to_db(item):
    cursor.execute("INSERT INTO Items VALUES (:Barcode, :Manufacturer, :Product, :Price, :Multiplier, :Quantity)",
                   {'Barcode': item.barcode, 'Manufacturer': item.manufacturer, 'Product': item.product,
                    'Price': item.price, 'Multiplier': item.multiplier, 'Quantity': item.quantity})
    connector.commit()


def add_quantity(barcode, number=1):
    # Check how many changes were made?  Idk, this should notify the user if quantity is not added.
    cursor.execute("UPDATE Items SET Quantity = Quantity + ? WHERE Barcode = ?", (str(number), barcode,))
    connector.commit()


def subtract_quantity(barcode, number=1):  # ROW IS EMPTY SO FOR LOOP NEVER HAPPENS
    try:
        quantity = cursor.execute("SELECT Quantity FROM Items WHERE Barcode = ?", (barcode,)).fetchone()[0]
    except TypeError:
        raise ValueError
    if quantity >= number:
        cursor.execute("UPDATE Items SET Quantity = ? WHERE Barcode = ?", (str(quantity-number), barcode,))
        connector.commit()
    else:
        raise ValueError


def get_name(barcode, get_manufacturer=True, get_product=True):
    info = cursor.execute("SELECT Manufacturer, Product FROM Items WHERE barcode = ?", (barcode,)).fetchone()
    if info is None:
        return None
    relevant = ''
    if get_manufacturer is True:
        relevant += info[0] + ' '
    if get_product is True:
        relevant += info[1]
    return relevant.strip()


def get_price(barcode, with_rewards=False):
    price = cursor.execute("SELECT Price, Multiplier FROM Items WHERE Barcode = ?", (barcode,)).fetchone()
    if price is None:
        return None
    if with_rewards is False:
        return format(price[0], '.2f')
    else:
        return format(price[0]*price[1], '.2f')


def get_quantity(barcode):
    try:
        return cursor.execute("SELECT Quantity FROM Items WHERE Barcode = ?", (barcode,)).fetchone()[0]
    except TypeError:
        return None


def set_manufacturer(barcode, manufacturer):
    cursor.execute("UPDATE Items SET Manufacturer = ? WHERE Barcode = ?", (manufacturer, barcode,))
    connector.commit()


def set_product(barcode, product):
    cursor.execute("UPDATE Items SET Product = ? WHERE Barcode = ?", (product, barcode,))
    connector.commit()


def set_quantity(barcode, number):
    cursor.execute("UPDATE Items SET Quantity = ? WHERE Barcode = ?", (str(number), barcode,))
    connector.commit()


def set_price(barcode, number):
    cursor.execute("UPDATE Items SET Price = ? WHERE Barcode = ?", (str(number), barcode,))
    connector.commit()


def set_multiplier(barcode, number):
    cursor.execute("UPDATE Items SET Price = ? WHERE Barcode = ?", (str(number), barcode,))
    connector.commit()


def extract_from_db(barcode):
    row = cursor.execute("SELECT * FROM Items WHERE Barcode=?", (barcode,)).fetchone()
    return Item(row[1], row[2], row[3], row[4], row[5], row[0])


def remove_from_db(barcode):
    cursor.execute("DELETE * FROM Items WHERE Barcode=?", (barcode,))
    connector.commit()
