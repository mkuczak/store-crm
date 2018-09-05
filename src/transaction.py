
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
        pass

    def remove_from_cart(self, number):
        pass

    def set_payment_method(self, payment_method):
        pass

    def set_card_number(self, card_number):
        pass
