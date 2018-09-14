from src.config import *
from src.item import *


def add_to_db(item):
    cursor.execute("INSERT INTO Items VALUES (:Barcode, :Manufacturer, :Product, :Price, :Multiplier, :Quantity)",
                   {'Barcode': item.barcode, 'Manufacturer': item.manufacturer, 'Product': item.product,
                    'Price': item.price, 'Multiplier': item.multiplier, 'Quantity': item.quantity})
    connector.commit()


def add_quantity(barcode, number=1):
    cursor.execute("UPDATE Items SET Quantity = Quantity + ? WHERE Barcode = '?'", number, barcode)
    connector.commit()


def subtract_quantity(barcode, number=1):  # ROW IS EMPTY SO FOR LOOP NEVER HAPPENS
    quantity = cursor.execute("SELECT Quantity FROM Items WHERE Barcode = '" + barcode + "'").fetchone()
    if quantity >= number:
        cursor.execute("UPDATE Items SET Quantity = ? WHERE Barcode = '?'", str(quantity-number), barcode)
        connector.commit()
    else:
        raise ValueError("Not enough items in stock. Quantity = " + str(quantity) + " | Number = " + str(number))


def get_name(barcode, get_manufacturer=True, get_product=True):
    info = cursor.execute("SELECT Manufacturer, Product FROM Items WHERE barcode = '?'", barcode)[0:1]
    relevant = ''
    if get_manufacturer is True:
        relevant += info[0] + ' '
    if get_product is True:
        relevant += info[1]
    return relevant.trim()


def get_price(barcode, with_rewards=False):
    price = cursor.execute("SELECT Price, Multiplier FROM Items WHERE Barcode = '?'", barcode).fetchone()
    if with_rewards is False:
        return price[0]
    else:
        return price[0]*price[1]


def get_quantity(barcode):
    return cursor.execute("SELECT Quantity FROM Items WHERE Barcode = '?'", barcode).fetchone()[0]


def set_manufacturer(barcode, manufacturer):
    cursor.execute("UPDATE Items SET Manufacturer = ? WHERE Barcode = '?'", manufacturer, barcode)


def set_product(barcode, product):
    cursor.execute("UPDATE Items SET Product = ? WHERE Barcode = '?'", product, barcode)


def set_quantity(barcode, number):
    cursor.execute("UPDATE Items SET Quantity = ? WHERE Barcode = '?'", str(number), barcode)
    connector.commit()


def set_price(barcode, number):
    cursor.execute("UPDATE Items SET Price = ? WHERE Barcode = '?'", str(number), barcode)
    connector.commit()


def set_multiplier(barcode, number):
    cursor.execute("UPDATE Items SET Price = ? WHERE Barcode = '?'", str(number), barcode)
    connector.commit()


def extract_from_db(barcode):
    row = cursor.execute("SELECT * FROM Items WHERE Barcode='?'", barcode).fetchone()
    return Item(row[1], row[2], row[3], row[4], row[5], row[0])


def remove_from_db(barcode):
    cursor.execute("DELETE * FROM Items WHERE Barcode='?'", barcode)
