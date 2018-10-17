import datetime
import sqlite3

global store_name
store_name = "X-Mart"
global phone_number
phone_number = "630-867-5309"
global city
city = "Istanbul"
global address
address = "619 N. Clark Rd."
global can_resell
can_resell = False


global connector
connector = sqlite3.connect(city + ".db")
connector.text_factory = str
global cursor
cursor = connector.cursor()

_cart_string = ""
for val in range(1,50):
    _cart_string += "Cart_" + str(val) + " text,\n"
_cart_string += "Cart_50 text\n)"
cursor.execute("""CREATE TABLE IF NOT EXISTS Transactions
                                            (ID int,
                                            Payment_Method text,
                                            Card_Number text,
                                            Rewards_ID int,
                                            """ + _cart_string)

cursor.execute("""CREATE TABLE IF NOT EXISTS Refunds
                                            (ID int,
                                            Reason text,
                                            """ + _cart_string.replace("Cart", "Item"))

cursor.execute("""CREATE TABLE IF NOT EXISTS Items
                                            (Barcode text,
                                            Manufacturer text,
                                            Product text,
                                            Price real,
                                            Multiplier real,
                                            Quantity int
                                            )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Manufacturers
                                            (Name text,
                                            Code text,
                                            Rule_1 text,
                                            Rule_2 text,
                                            Rule_3 text,
                                            Rule_4 text,
                                            Rule_5 text
                                            )""")


def date_time(exp=None):
    if exp is None:
        dt = datetime.datetime.now()
    else:
        dt = datetime.datetime.now() + datetime.timedelta(days=90)
    month = str(dt.month)
    day = str(dt.day)
    year = str(dt.year)
    hour = str(dt.hour)
    minute = str(dt.minute)
    if len(str(dt.minute)) == 1:
        minute = '0' + minute
    return month + '/' + day + '/' + year + ' ' + hour + ':' + minute
