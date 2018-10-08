from src.config import *
from src.manufacturer import *


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
    row = cursor.execute("SELECT * FROM Manufacturers WHERE Name = ?", (name,)).fetchone()
    if row is None:
        raise ValueError
    else:
        rules = []
        for n in range(2, 6):
            if row[n] != "":
                rules.append(row[n])
        return Manufacturer(row[0], row[1], rules)


def extract_from_db_by_code(code):
    row = cursor.execute("SELECT * FROM Manufacturers WHERE Code = ?", (code,)).fetchone()
    if row is None:
        raise ValueError
    else:
        rules = []
        for n in range(2, 6):
            if row[n] != "":
                rules.append(row[n])
        return Manufacturer(row[0], row[1], rules)


def remove_from_db_by_name(name):
    cursor.execute("DELETE * FROM Manufacturers WHERE Name = ?", (name,))
    connector.commit()


def remove_from_db_by_code(code):
    cursor.execute("DELETE * FROM Manufacturers WHERE Code = ?", (code,))
    connector.commit()


def get_name_from_code(code):
    try:
        return cursor.execute("SELECT Name FROM Manufacturers WHERE Code = ?", (code,)).fetchone()[0]
    except TypeError:
        return None


def get_code_from_name(name):
    try:
        return cursor.execute("SELECT Code FROM Manufacturers WHERE Name = ?", (name,)).fetchone()[0]
    except TypeError:
        return None


def get_rules_from_code(code):
    _rules = []
    row = cursor.execute("SELECT Rule_1, Rule_2, Rule_3, Rule_4, Rule_5 FROM Manufacturers WHERE Code = ?", (code,))
    if row is None:
        return None
    for i in range(2, 7):
        _rule = cursor.fetchone()[i]
        if _rule == "":
            break
        else:
            _rules.append(_rule)
    return _rules


def get_rules_from_name(name):
    _rules = []
    row = cursor.execute("SELECT Rule_1, Rule_2, Rule_3, Rule_4, Rule_5 FROM Manufacturers WHERE Name = ?", (name,))
    if row is None:
        return None
    for i in range(2, 7):
        _rule = cursor.fetchone()[i]
        if _rule == "":
            break
        else:
            _rules.append(_rule)
    return _rules
