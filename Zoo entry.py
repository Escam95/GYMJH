process_success = False
year = False
ages = []
prices = []
check = 0
price = 0
cost = 0
insert = 0


def eligable_num(que):
    global process_success, check
    while not process_success:
        try:
            check = int(input(que))
            if check > 0 and check is not float:
                return check
            else:
                print("That is not a valid number.")
                process_success = False
        except ValueError or TypeError or NameError:
            print("That is not a valid number.")


for t in range(0, 1):
    time = input('What kind of entry would you like to purhcase?\nFor a day entry press D,\nfor a year entry press '
                 'R\n> ')
    if time == "D":
        year = False
    elif time == 'R':
        year = True
    elif time == '':
        exit()
    else:
        print('Not what I am looking for, try again.\n')
        continue
    que = "For how many people are you buing a ticket?\n> "
    persons = eligable_num(que)
    for person in range(0, persons):
        factor = 30
        print(str(person + 1) + '. Person')
        que = "Age: "
        age = eligable_num(que)
        if 2 < age < 16:
            factor = 20
            print('Category: Child')
        elif age > 65:
            factor = 15
            print('Category: Pensioner')
        elif age < 3:
            print("Free entry")
            continue
        else:
            print('Category: Adult')
        if year:
            if factor == 20:
                price = factor * 5 * 9
            elif factor == 15:
                price = factor * 10 * 4
            else:
                price = factor * 10 * 6
        elif not year:
            price = factor * 10
        print('Price: ' + str(price))
        prices.append(price)
        ages.append(age)
    print(ages)
    print(prices)
    for price in range(0, len(prices)):
        cost += prices[price]
    print('Your final cost is: ' + str(cost) + '\n')
    while insert < cost:
        que = "Please insert money: "
        bill = eligable_num(que)
        if bill == 10 or bill == 20 or bill == 50 or bill == 100 or bill == 200 or bill == 500 or bill == 1000\
                or bill == 5000:
            insert += bill
            print('Inserted so far: ' + str(insert))
        else:
            print('Not an eligable bill.')
            continue
    print('Returning money, please wait...')
    while insert > cost:
        if insert - 500 - cost >= 0:
            insert -= 500
            print('500,-')
        elif insert - 200 - cost >= 0:
            insert -= 200
            print('200,-')
        elif insert - 100 - cost >= 0:
            insert -= 100
            print('100,-')
        elif insert - 50 - cost >= 0:
            insert -= 50
            print('50,-')
        else:
            print('The rest is ours to take ;]')
            break
    print('\nThank you for your purchase')
