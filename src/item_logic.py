from src.item import Item

import src.itemDB as itemDB
import src.manufacturerDB as manufacturerDB

from src.prompt import sep, options
import src.prompt as prompt


def new():
    sep()
    name = input("Input the name of this item: ")
    while True:
        sep()
        n = prompt.mc("Assign a manufacturer to the item", options, "Input by name", "Input by code", "Cancel item")[1]
        sep()
        if n == 1:
            m_info = prompt.ff("Manufacturer by name", "Name", manufacturerDB.get_code_from_name)
            if m_info is None:
                continue
            else:
                m_code = m_info[0]
                m_name = m_info[1]
                break
        elif n == 2:
            m_info = prompt.ff("Manufacturer by code", "Code", manufacturerDB.get_name_from_code)
            if m_info is None:
                continue
            else:
                m_name = m_info[0]
                m_code = m_info[1]
                break
        elif n == 3:
            return
    while True:
        sep()
        n = prompt.mc("Input the price of the item", options, "Input price", "Skip", "Cancel item")[1]
        if n == 1:
            try:
                price = input("Price: ")
                if price == "":
                    continue
                else:
                    price = float(price)
                    break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 2:
            price = float(0.00)
            break
        elif n == 3:
            return
    while True:
        sep()
        n = prompt.mc("Determine the rewards benefits of the item", options,
                      "No discount", "Input percent discount", "Input modified price", "Cancel item")[1]
        if n == 1:
            multiplier = float(1.00)
            break
        elif n == 2:
            try:
                percent = input("Percent off: ")
                multiplier = (100-float(percent))*0.01
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 3:
            try:
                modified_price = float(input("Modified price: "))
                multiplier = modified_price/price
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 4:
            return
    while True:
        sep()
        n = prompt.mc("Input the quantity of the item", options, "Input quantity", "Skip", "Cancel item")[1]
        if n == 1:
            try:
                quantity = int(input("Quantity: "))
                break
            except ValueError:
                print("Invalid input.")
                continue
        elif n == 2:
            quantity = 0
            break
        elif n == 3:
            return
    item = Item(m_name, name, price, multiplier, quantity)
    while True:
        i = 0
        sep()
        n = prompt.mc("Input the 5-digit code for this product", options, "Input code", "Auto-select", "Cancel item")[1]
        sep()
        if n == 1:
            p_code = input("Code: ")
            if p_code.isdigit() and len(p_code) == 5:
                try:
                    item.build_barcode('0', m_code, p_code)
                    break
                except ValueError:
                    print("An identical barcode already exists in the database.")
            else:
                print("Invalid input.")
                continue
        elif n == 2:
            while True:
                i += 1
                p_code = str(i)
                while len(p_code) < 5:
                    p_code = '0' + p_code
                try:
                    item.build_barcode('0', m_code, p_code)
                    break
                except ValueError:
                    continue
            break
        elif n == 3:
            return

    itemDB.add_to_db(item)
    print(name + " successfully added to the item database.")


def search():
    extraction = prompt.ff("Items -> Search", "Barcode", itemDB.extract_from_db)
    sep()
    extraction.print_data()
    sep()
