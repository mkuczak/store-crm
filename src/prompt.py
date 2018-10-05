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
            print("ValueError: Try again.\n")


# Multiple Choice Prompt: Options are listed and the user only needs to select an int from the list.
def mc(heading, func, *choices):
    while True:
        print(heading)
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
            n += 1
        try:
            decision = int(input("Input value: "))
            func(decision)
            break
        except ValueError:
            print("ValueError: Try again.\n")
        except IndexError:
            print("IndexError: Try again.\n")


# Free Form Prompt: User must input something (such as a barcode) with the heading being the only guidance.
def ff(heading, keyword, func):
    while True:
        print(heading)
        try:
            user_input = input("Input " + keyword + ": ")
            return func(user_input), user_input
        except ValueError:
            print("ValueError: Try again.\n")
        except AssertionError:
            print("AssertionError: Try again.\n")