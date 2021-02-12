

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(
            f'Enter an option ({option_string}): '
        )
        if choice in options:
            return options[choice]()
        print('Not a valid option')

def func_b():
    return "B"

def func_a():
    return "A"

menu_values = menu(a=func_a, b=func_b)
print(f'Result is {menu_values}')

