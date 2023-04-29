import datetime as dt

process_success = False
year = False
ages = []
prices = []
codes = []
cats = []
check = 0
price = 0
cost = 0
insert = 0
code = 0
count = 1


def eligible(que):
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


def border():
    for i in range(0, 17):
        print('=', end='')
    print()


for t in range(0, 1):
    time = input('What kind of entry would you like to purchase?\nFor a day entry press D,\nfor a year entry press '
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
    que = "For how many people are you buying a ticket?\n> "
    persons = eligible(que)
    for person in range(0, persons):
        factor = 30
        print(str(person + 1) + '. Person')
        que = "Age: "
        age = eligible(que)
        if 2 < age < 16:
            factor = 20
            code = 22
            cat = 'Child'
        elif age > 65:
            factor = 15
            code = 24
            cat = 'Pensioner'
        elif age < 3:
            print("Free entry")
            continue
        else:
            code = 11
            cat = 'Adult'
        print('Category: ' + cat)
        if year:
            if factor == 20:
                price = factor * 5 * 9
                code = 42
            elif factor == 15:
                price = factor * 10 * 4
                code = 44
            else:
                price = factor * 10 * 6
                code = 33
        elif not year:
            price = factor * 10
        print('Price: ' + str(price))
        cats.append(cat)
        codes.append(code)
        prices.append(price)
        ages.append(age)
    print(ages)
    print(prices)
    for price in range(0, len(prices)):
        cost += prices[price]
    print('Your final cost is: ' + str(cost) + '\n')
    while insert < cost:
        que = "Please insert money: "
        bill = eligible(que)
        if bill == 10 or bill == 20 or bill == 50 or bill == 100 or bill == 200 or bill == 500 or bill == 1000\
                or bill == 5000:
            insert += bill
            print('Inserted so far: ' + str(insert))
        else:
            print('Not an eligible bill.')
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
    print("\nThank you for your purchase\n\nHere are your tickets:\n")
    date = dt.date.today().strftime("%y%m%d")
    for i in range(0, len(ages)):
        divide = 0
        code_sum = 0
        for j in range(0, len(date)):
            divide += int(date[j])
        for j in range(0, len(str(codes[i]))):
            code_num = str(codes[i])
            code_sum += int(code_num[j])
        new_divide = divide + code_sum + count
        last = 0
        while (new_divide + last) % 10 != 0:
            last += 1
        spec = date + str(codes[i]) + (4-len(str(count))) * '0' + str(count) + str(last)
        count += 1
        border()
        spaces = (12 - len(cats[i]))
        print('| ZOO PRAHA     |\n| 1 ' + cats[i] + spaces*' ' + '|\n| ' + spec + ' |')
        border()
        print()
    print('Enjoy your stay!')
