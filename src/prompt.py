def navigate_menu(heading, *choices):
    while True:
        print("- " + heading + " -")
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        if heading != "Main Menu":
            print("0: Main Menu")
        try:
            decision = int(input("Input value: "))
            if 0 <= int(decision) <= n:
                return decision
        except ValueError:
            print("ValueError: Try again.")
            sep()


# Multiple Choice Prompt: Options are listed and the user only needs to select an int from the list.
def mc(heading, func, *choices):
    while True:
        print(heading)
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        try:
            decision = input("Input value: ")
            if decision == "":
                return None
            return func(decision), int(decision)
        except ValueError:
            print("ValueError: Try again.")
            sep()
        except IndexError:
            print("IndexError: Try again.")
            sep()


# Free Form Prompt: User must input something (such as a barcode) with the heading being the only guidance.
def ff(heading, keyword, func, extra_input=None):
    while True:
        print(heading)
        try:
            user_input = input("Input " + keyword + ": ")
            if user_input == "":
                return None
            if extra_input is None:
                return func(user_input), user_input
            else:
                return func(user_input, extra_input), user_input
        except ValueError:
            print("ValueError: Try again.")
            sep()
        except AssertionError:
            print("AssertionError: Try again.")
            sep()


def sep():
    print("------------------------------")


def options(n):
    return n
