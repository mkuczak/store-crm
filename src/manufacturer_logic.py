from src.manufacturer import Manufacturer

import src.manufacturerDB as manufacturerDB

from src.prompt import sep, options
import src.prompt as prompt


def new():
    sep()
    while True:
        print("Input manufacturer name")
        name = input("Name: ")
        copy = manufacturerDB.get_code_from_name(name)
        if copy is None:
            break
        else:
            sep()
            print(name + " is being used by another manufacturer (code: " + copy + ")")
    sep()
    while True:
        print("Input 5-digit code")
        code = input("Code: ")
        if code.isdigit() and len(code) == 5:
            copy = manufacturerDB.get_name_from_code(code)
            if copy is None:
                break
            else:
                sep()
                print(copy + " is already using the code " + code)
        else:
            sep()
            print(code + " is an invalid 5-digit code")
    rules = []
    sep()
    while True:
        n = prompt.mc("Would you like to add product code rules to this manufacturer?", options, "Yes", "No",
                      "Cancel manufacturer")[1]
        if n == 1:
            my_rule = input("Rule " + str(len(rules) + 1) + ": ")
            rules.append(my_rule)
            sep()
            print("Current rules: ")
            for rule in rules:
                print("- " + rule)
            sep()
        elif n == 2:
            break
        elif n == 3:
            sep()
            return
        else:
            sep()
            print("Invalid input")
    sep()
    manufacturerDB.add_to_db(Manufacturer(name, code, rules))
    print(name + " successfully added to the manufacturer database.")
    sep()


def search(code):
    if code is False:
        extraction = prompt.ff("Manufacturers -> Search", "Name", manufacturerDB.extract_from_db_by_name)[0]
    else:
        extraction = prompt.ff("Manufacturers -> Search", "Code", manufacturerDB.extract_from_db_by_code)[0]
    sep()
    extraction.print_data()
    sep()
    # Add edit features, create a way out, and prevent it from breaking when blank input is given
