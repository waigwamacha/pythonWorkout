

MENU = {
    'gatheri': 120,
    'mukimo': 150,
    'mataha': 200,
    'pilau': 350,
    'chemsha': 180,
    'choma ugali': 300,
    'chapati mix': 200,
}

def restaurant():
    total = 0
    while True:
        order = input('Enter the dish you would like today: ').strip() #removing whitespace
        if order in MENU.keys():
            print(f"Order: {order}")
            price = MENU[order]
            total += price
            print(f"{order} costs {MENU[order]}, total is {total}")
        elif order == "":
            break
        else:
            print(f"We don't have {order} today. Try something else:")
    print(f"Your total is {total}")

# restaurant()

PASSWORDS = {
    'testuser': 'kamausteven',
    'superuser': 'adminpass',
}

def password_check():
    counter = 3
    done= False
    username = input("Enter your username (press q to exit): ").strip().lower()
    password = input("Enter password: ").strip().lower()
    while done is False:
        if username not in PASSWORDS.keys() or username == 'q':
            print("username not registered")
            counter -= 1
            # break
        if username in PASSWORDS and password == PASSWORDS[username]:
            print(f"{username} logged in!")
            done =True 
        if counter == 0:
            print("Reached try limits. Try in 30 seconds!")
            break

# password_check()
TEMPS = {
    'monday': 24,
    'tuesday': 31,
    'wednesday': 20,
    'thursday': 25,
    'friday': 26,
    'saturday': 34,
}

def temperatures():
    date = input("Enter a date of the week and I'll show you it's recored temperature: ").strip().lower()
    while True:
        if date not in TEMPS.keys():
            print("That's not a valid date!")
            break
        if date in TEMPS.keys():
            print(f"The temperature on {date} was {TEMPS[date]}")
            # print('__*5')
            break

BIRTHDATES = {
    'monday': 24,
    'tuesday': 31,
    'wednesday': 20,
    'thursday': 25,
    'friday': 26,
    'saturday': 34,
}

# temperatures()

def get_rainfall():
    """get rainfall data (city, rainfall(mm)) and saves it in a dictionary"""
    rain_data = {}
    while True:
        city = input("Enter city name: ").strip()
        if not city or city == 'q':
            break
        try:
            rain_amount = int(input("Enter amount of rain in mm: "))
        except ValueError:
            print("You need to input a number for rain amount (mm)!")
            continue
        rain_data[city] = rain_data.get(city, 0) + int(rain_amount)
        for city, rain in rain_data.items():
            print(f"City: {city}, mm: {rain}")
        print(rain_data)
            
# get_rainfall()

def dictdiff(d1, d2):
    """Takes two dictionaries and returns their difference

    Args:
        d1 (: [1st dictionary]
        d2 : [2nd dictionary]
    """
    diff = {}
    for key, value in d1.items():
        if key not in d2.keys() or value not in d2.values():
            diff[key] = [diff.get(key, 0) + d1[key], d2[key]]
    print(diff)

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
# dictdiff(d1, d2)

def dictdiff2(first, second):

    output = {}
    all_keys = first.keys() | second.keys()
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key,), second.get(key)]
    return output

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
# print(dictdiff2(d3, d4))


def how_many_different_numbers(thislist):
    uniq_nums = set()
    for num in thislist:
        uniq_nums.add(num)
    return len(uniq_nums)

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
# print(how_many_different_numbers(numbers))

def mergedicts(first, second):
    """merges any number of dicts into one dict"""
    output = {**first, **second}
    for key, value in output.items():
        if key in first and key in second:
            output[key] = first[key], second[key]
    return output

# print(mergedicts(d3, d4))

def mergeanydicts(*manydicts):
    output = {}
    for dictionary in manydicts:
        output.update(dictionary)
    return output

print(d1)
print(d2)
print(d3)
print(mergeanydicts(d1, d2, d3))