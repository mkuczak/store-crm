class Item:

    def __init__(self, manufacturer, product, price, multiplier, quantity, barcode=None):
        if barcode is None:
            self.barcode = ""
        else:
            self.barcode = barcode
        self.manufacturer = manufacturer
        self.product = product
        self.price = price
        self.multiplier = multiplier
        self.quantity = quantity

    def build_barcode(self, first, manufacturer_code, product_code):
        b = [int(first)]
        for n in manufacturer_code:
            b.append(int(n))
        for n in product_code:
            b.append(int(n))
        # Below is the logic for the check digit.  Read more about it here:
        # http://www.azalea.com/white-papers/upc-barcode-check-digit/
        check_digit = str((10 - (3*(b[0]+b[2]+b[4]+b[6]+b[8]+b[10])+(b[1]+b[3]+b[5]+b[7]+b[9]))) % 10)
        barcode = ""
        for n in b:
            barcode += str(n)
        barcode += check_digit
        self.barcode = barcode
