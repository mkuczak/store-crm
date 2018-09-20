def main():
    #numbered_prompt("Remove what?", refund.remove_from_items(), ["This", "That"])
    pass


def numbered_prompt(heading, func, choices):
    while True:
        print(heading)
        n = 1
        for choice in choices:
            print(str(n) + ': ' + choice)
        try:
            func(int(input("Input value: ")))
            break
        except ValueError:
            print("ValueError: Try again.\n")
        except IndexError:
            print("IndexError: Try again.\n")
        except AssertionError:
            print("AssertionError: Try again.\n")


main()
