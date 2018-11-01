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
            if m_info[0] is None:
                sep()
                print("Manufacturer does not exists.")
                continue
            else:
                m_code = m_info[0]
                m_name = m_info[1]
                break
        elif n == 2:
            m_info = prompt.ff("Manufacturer by code", "Code", manufacturerDB.get_name_from_code)
            if m_info[0] is None:
                sep()
                print("Manufacturer does not exists.")
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
        sep()
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
        sep()
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
    sep()
    print(name + " successfully added to the item database.")
    print("Barcode given: " + item.barcode)
    sep()


def search():
    sep()
    extraction = prompt.ff("Items -> Search", "Barcode", itemDB.extract_from_db)
    if extraction is not None:
        item = Item(extraction[0][0], extraction[0][1], extraction[0][2],
                    extraction[0][3], extraction[0][4], extraction[0][5])
        barcode = extraction[1]
        while True:
            sep()
            item.print_data()
            sep()
            try:
                n = prompt.mc("Edit item values?", options, "Return to main menu", "Quantity", "Price", "Discount")[1]
                sep()
                if n == 1:
                    sep()
                    return
                elif n == 2:
                    try:
                        n = prompt.mc("Edit item quantity options", options, "Return to main menu", "Set total",
                                      "Add to total", "Subtract from total")[1]
                    except TypeError:
                        sep()
                        print("Not a valid price. Returning to main menu.")
                        sep()
                        return
                    except ValueError:
                        sep()
                        print("Not a valid price. Returning to main menu.")
                        sep()
                        return
                    sep()
                    if n == 1:
                        return
                    elif n == 2:
                        try:
                            ans = prompt.ff("Set total number of " + item.product + " in stock", "Total", options)[1]
                        except TypeError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        except ValueError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        sep()
                        if ans is None:
                            sep()
                            print("Operation cancelled.")
                        else:
                            try:
                                item.quantity = int(ans)
                                itemDB.set_quantity(barcode, item.quantity)
                                print("Quantity successfully adjusted.")
                            except ValueError:
                                sep()
                                print("Invalid input.")
                        continue
                    elif n == 3:
                        try:
                            ans = prompt.ff("Adding to current value of " + str(item.quantity), "Value", options)[1]
                        except TypeError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        except ValueError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        sep()
                        if ans is None:
                            sep()
                            print("Operation cancelled.")
                        else:
                            try:
                                item.quantity = item.quantity + int(ans)
                                itemDB.add_quantity(barcode, item.quantity)
                                print("Quantity successfully adjusted.")
                            except ValueError:
                                sep()
                                print("Invalid input.")
                        continue
                    elif n == 4:
                        try:
                            ans = prompt.ff("Subtracting from current value of " + str(item.quantity), "Value",
                                            options)[1]
                        except TypeError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        except ValueError:
                            sep()
                            print("Not a valid price. Returning to main menu.")
                            sep()
                            return
                        sep()
                        if ans is None:
                            sep()
                            print("Operation cancelled.")
                        else:
                            try:
                                item.quantity = item.quantity - int(ans)
                                itemDB.subtract_quantity(barcode, int(ans))
                                print("Quantity successfully adjusted.")
                            except ValueError:
                                sep()
                                print("Invalid input.")
                elif n == 3:
                    try:
                        n = prompt.ff("Edit item price (current: " + str(item.price) + ")", "Price", options)[1]
                        n = float(n)
                        item.price = n
                        itemDB.set_price(barcode, item.price)
                        sep()
                        print("Price successfully adjusted.")
                    except TypeError:
                        sep()
                        print("Not a valid price. Returning to main menu.")
                        sep()
                        return
                    except ValueError:
                        sep()
                        print("Not a valid price. Returning to main menu.")
                        sep()
                        return
                elif n == 4:
                    try:
                        n = prompt.mc("Edit item discount options", options, "Return to main menu", "Set percent off",
                                      "set multiplier")[1]
                        sep()
                        if n == 1:
                            return
                        elif n == 2:
                            try:
                                ans = prompt.ff("Set percent off", "Percent", options)[1]
                            except ValueError or TypeError:
                                sep()
                                print("Returning to main menu.")
                                sep()
                                return
                            sep()
                            if ans is None:
                                sep()
                                print("Operation cancelled.")
                            else:
                                try:
                                    item.multiplier = 100.00 - float(ans)
                                    itemDB.set_quantity(barcode, item.multiplier)
                                    print("Percent off successfully adjusted.")
                                except ValueError:
                                    sep()
                                    print("Invalid input.")
                        elif n == 3:
                            try:
                                ans = prompt.ff("Set multiplier", "Multiplier", options)[1]
                            except ValueError or TypeError:
                                sep()
                                print("Returning to main menu.")
                                sep()
                                return
                            sep()
                            if ans is None:
                                sep()
                                print("Operation cancelled.")
                            else:
                                try:
                                    item.multiplier = float(ans)
                                    itemDB.set_quantity(barcode, item.multiplier)
                                    print("Multiplier successfully adjusted.")
                                except ValueError:
                                    sep()
                                    print("Invalid input.")
                    except ValueError:
                        sep()
                        print("Returning to main menu.")
                        sep()
                        return
                continue
            except ValueError:
                sep()
                print("Invalid input. Returning to main menu.")
                sep()
                return
    else:
        sep()
        print("Item not found in database.")
        sep()
