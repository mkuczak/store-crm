class Refund:

    def __init__(self, t_id, items=None, reason=None):
        self.t_id = t_id
        if items is None:
            self.items = []
        else:
            self.items = items
        self.reason = reason

    def add_to_items(self, barcode, cart):
        b_score = 0
        for item in self.items:
            if item == barcode:
                b_score -= 1
        for item in cart:
            if item == barcode:
                b_score += 1
        if b_score > 0:
            self.items.append(barcode)
        else:
            raise ValueError

    def add_all_to_items(self, cart):
        self.items = cart

    def remove_from_items(self, number):
        number = int(number)  # Raises ValueError if number is not made up of digits
        if number < 1:
            raise ValueError
        elif number > len(self.items):
            raise IndexError
        else:
            self.items.pop(number - 1)