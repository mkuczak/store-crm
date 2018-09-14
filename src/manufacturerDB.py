from src.config import*
from src.manufacturer import*


def add_to_db(manufacturer):
    _rules = []
    for n in range(0, 5):
        try:
            _rules.append(manufacturer.rules[n])
        except IndexError:
            _rules.append("")
    cursor.execute("INSERT INTO Manufacturers VALUES (:Manufacturer, :Code, :Rule_1, :Rule_2, :Rule_3, :Rule_4,"
                   ":Rule_5)",
                   {'Manufacturer': manufacturer.name, 'Code': manufacturer.code,
                    'Rule_1': _rules[0], 'Rule_2': _rules[1], 'Rule_3': _rules[2], 'Rule_4': _rules[3],
                    'Rule_5': _rules[4]})
    connector.commit()


def extract_from_db_by_name(name):
    row = cursor.execute("SELECT * FROM Manufacturers WHERE Name='?'", name).fetchone()
    return Manufacturer(row[0], row[1], [row[2], row[3], row[4], row[5], row[6], row[7]])


def extract_from_db_by_code(code):
    row = cursor.execute("SELECT * FROM Manufacturers WHERE Code='?'", code).fetchone()
    return Manufacturer(row[0], row[1], [row[2], row[3], row[4], row[5], row[6], row[7]])


def remove_from_db_by_name(name):
    cursor.execute("DELETE * FROM Manufacturers WHERE Name='?'", name)


def remove_from_db_by_code(code):
    cursor.execute("DELETE * FROM Manufacturers WHERE Code='?'", code)


def get_name_from_code(code):
    return cursor.execute("SELECT Name FROM Manufacturers WHERE Code='?'", code).fetchone()[0]


def get_code_from_name(name):
    return cursor.execute("SELECT Code FROM Manufacturers WHERE Name='?'", name).fetchone()[1]


def get_rules_from_code(code):
    _rules = []
    cursor.execute("SELECT Rule_1, Rule_2, Rule_3, Rule_4, Rule_5 FROM Manufacturers WHERE Code='?'", code)
    for i in range(2, 7):
        _rules.append(cursor.fetchone()[i])
    return _rules


def get_rules_from_name(name):
    _rules = []
    cursor.execute("SELECT Rule_1, Rule_2, Rule_3, Rule_4, Rule_5 FROM Manufacturers WHERE Name='?'", name)
    for i in range(2, 7):
        _rules.append(cursor.fetchone()[i])
    return _rules
