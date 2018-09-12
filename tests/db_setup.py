import sqlite3


def finish(num):
    fin = ""
    for i in range(0, num):
        fin += ", ''"
    return fin + ')'


t_connector = sqlite3.connect('test.db')
t_connector.text_factory = str
t_cursor = t_connector.cursor()

cart_string = ""
for val in range(1, 50):
    cart_string += "Cart_" + str(val) + " text,\n"
cart_string += "Cart_50 text\n)"
t_cursor.execute("""CREATE TABLE IF NOT EXISTS Transactions
                                            (ID int,
                                            Payment_Method text,
                                            Card_Number text,
                                            Rewards_ID int,
                                            """ + cart_string)
t_cursor.execute("""CREATE TABLE IF NOT EXISTS Refunds
                                            (ID int,
                                            Reason text,
                                            """ + cart_string.replace("Cart", "Item"))
t_cursor.execute("""CREATE TABLE IF NOT EXISTS Items
                                            (Barcode text,
                                            Manufacturer text,
                                            Product text,
                                            Price real,
                                            Multiplier real,
                                            Quantity int
                                            )""")
t_cursor.execute("""CREATE TABLE IF NOT EXISTS Manufacturers
                                                (Name text,
                                                Code text,
                                                Rule_1 text,
                                                Rule_2 text,
                                                Rule_3 text,
                                                Rule_4 text,
                                                Rule_5 text
                                                )""")

t_cursor.execute("DELETE FROM Transactions")
t_cursor.execute("DELETE FROM Refunds")
t_cursor.execute("DELETE FROM Items")
t_cursor.execute("DELETE FROM Manufacturers")

t_cursor.execute("""INSERT INTO Transactions VALUES (1, 'Credit', '0000111122223333', 0, '000111222333', '444555666777',
                '888999000111'""" + finish(47))
t_cursor.execute("""INSERT INTO Transactions VALUES (2, 'Cash', '', 0, '000111222333', '444555666777',
                '888999000111', '222333444555'""" + finish(46))
t_cursor.execute("""INSERT INTO Transactions VALUES (3, 'Credit', '1234123412341234', 0, '000000111111', '444555666777',
                '111222333444', '444555666777', '000001111100'""" + finish(45))

t_cursor.execute("""INSERT INTO Refunds VALUES (2, '', '000111222333', '444555666777', '888999000111', '222333444555'"""
               + finish(46))
t_cursor.execute("""INSERT INTO Refunds VALUES (3, 'Expired product', '000000111111'""" + finish(49))

t_cursor.execute("""INSERT INTO Items VALUES ('016000275270', "General Mills", "Honey Nut Cheerios Cereal - 12oz",
               3.99, 1.00, 90)""")
t_cursor.execute("""INSERT INTO Items VALUES ('051500006771', "Smucker's", "Smucker's: Cherry Preserves - 18oz",
               4.55, 0.85, 0)""")

t_cursor.execute("""INSERT INTO Manufacturers VALUES ("General Mills", '16000', 'Do not pick up the phone',
               'Do not let him in'""" + finish(3))
t_cursor.execute("""INSERT INTO Manufacturers VALUES ("Smucker's", '51500', 'Do not be his friend',
               'You know that you will be waking up in his bed in the morning', 'If you are under him'""" + finish(2))

t_connector.commit()
