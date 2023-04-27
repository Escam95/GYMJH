process_success = False
ages = []


def eligable_num(string):
    global process_success, check
    while not process_success:
        try:
            check = int(input(string))
            if check > 0 and check is not float:
                porcess_success = True
                return check
            else:
                print("That is not a valid number.")
                process_success = False
        except ValueError or TypeError or NameError:
            print("That is not a valid number.")


while True:
    time = input('What kind of entry would you like to purhcase?\nFor a day entry press D,\nfor a year entry press '
                 'R\n> ')
    string = "For how many people are you buing a ticket?\n> "
    persons = eligable_num(string)
    for person in range(0, persons):
        string = "Age: "
        ages.append(eligable_num(string))
    print(ages)
