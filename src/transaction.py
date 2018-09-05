
class Transaction:

    def __init__(self, cart=None, payment_method=None, card_number=None, rewards_id=None):
        if cart is None:
            self.cart = []
        else:
            self.cart = cart
        if payment_method is None:
            self.payment_method = ""
        else:
            self.payment_method = payment_method
        if card_number is None:
            self.card_number = ""
        else:
            self.card_number = card_number
        if rewards_id is None:
            self.rewards_id = 0
        else:
            self.rewards_id = rewards_id

    def add_to_cart(self, barcode):
        self.cart.append(barcode)

    def remove_from_cart(self, number):
        number = int(number)  # Raises ValueError if number is not made up of digits
        if number < 1:
            raise ValueError
        elif number > len(self.cart):
            raise IndexError
        else:
            self.cart.pop(number - 1)

    def set_payment_method(self, payment_method):
        if (payment_method == "credit" or payment_method == "debit" or
                payment_method == "cash" or payment_method == "check"):
            self.payment_method = payment_method
        else:
            raise ValueError

    def set_card_number(self, card_number):
        if len(card_number) != 16:
            raise ValueError
        elif card_number.isdigit() is False:
            raise ValueError
        elif self.payment_method != "credit" and self.payment_method != "debit":
            raise AssertionError
        else:
            self.card_number = card_number

