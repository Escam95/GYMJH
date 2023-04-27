process_success = False


def eligable_num(check):
    global process_success
    try:
        check = int(check)
    except ValueError or TypeError:
        print("That is not a valid number.")
    if check > 0 and check is not float:
        porcess_success = True
    else:
        print("That is not a valid number.")
        process_success = False


while True:
    time = input('What kind of entry would you like to purhcase?\nFor a day entry press D,\nfor a year entry press '
                 'R\n> ')
    while not process_success:
        check = input("For how many people are you buing a ticket?\n> ")
        eligable_num(check)
    process_success = False
