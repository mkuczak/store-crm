class Manufacturer:

    def __init__(self, name, code, rules = None):
        self.name = name
        self.code = code
        if rules == None:
            self.rules = []
        else:
            self.rules = rules

    # numbers rules and returns them as a string.  Menu will display this when asking user to input a product code.
    def list_rules(self):
        numbered_rules = ""
        number = 1
        for rule in self.rules:
            numbered_rules += "(" + str(number) + ") " + rule + "\n"
            number += 1
        numbered_rules = numbered_rules[:-1]
        if numbered_rules == "":
            return "No rules have been set for this manufacturer."
        else:
            return numbered_rules

    # If no number given, places rule at the end.  Otherwise, shifts rules to the right.
    def add_rule(self, rule, number=None):
        if number == None:
            self.rules.append(rule)
        else:
            self.rules.insert(number-1, rule)

    # Removes selected rule and shifts rules to the left
    def remove_rule(self, number):
        number = int(number)
        if number >= 1:
            self.rules.pop(number-1)
        else:
            raise ValueError

    def remove_all_rules(self):
        self.rules = []
