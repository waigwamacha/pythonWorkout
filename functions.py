import operator, random
import re 

def myxml(parent, child='', **kwargs):
    """
    function that takes a number of arguments and prints an xml output
    """
    pair = ''.join([f"{key}='{value}'" for key, value in kwargs.items()])
    print(f'<name, {pair}>{child}</name>')

# myxml('parent', 'child', a=1, b=3, c=5)

def copyfile(file1, somefile='', *args): #Incomplete 
    """
    function that takes a file, file1, and makes copies of it
    """
    with open(file1) as infile:
        for files in args():
            files.copy(infile)
            print(files)

# copyfile('lines.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')

def mycalc():
    """
    accepts a string and performs arithmetic calculations on it in prefix notation
    """
    thiscalc = input('enter two numbers to perform arithmetic on (e.g. + 2 3): ')
    list = []
    symbol = []
    for numbers in thiscalc:
        if numbers != ' ' and numbers != 'None':
            list.append(numbers[0:])
    symbol = list.pop(0)
    # print(list)
    int_list = []
    ans = 0
    for items in list:
        int_list.append(int(items))
    # print(int_list)
    # print(int_list[0])
    # print(int_list[1])
    for item in int_list:
        if symbol == '+':
            ans = int_list[0] + int_list[1]
        elif symbol == '-':
            ans = int_list[0] - int_list[1]
        elif symbol == '*':
            ans = (int_list[0])*(int_list[1])
        # elif symbol == '**':
        #     ans = (int_list[0])**(int_list[1])
        elif symbol == '/':
            ans = (int_list[0])/(int_list[1])


    print(ans)
    
# mycalc()

def calc(to_solve):
    operations = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv,
                    '**': operator.pow,
                    '%': operator.mod}

    op, first_s, second_s = to_solve.split(maxsplit=3)
    first = int(first_s)
    second = int(second_s)
    return operations[op](first, second)


# print(calc('/ 3 4'))

def create_pass(pass_str):
    def alpha_pass(an_int):
        output = []
        for item in range(an_int):
            output.append(random.choice(pass_str))
            # passwd = ''.join([random.choice(pass_str) for item in range(an_int)])
        return ''.join(output)
    return alpha_pass

x = create_pass('abcdef')
print(x(5))
symbol_pass = create_pass('!@#$%')
print(symbol_pass(10))

def passwd_checker():
    """
    verifies that an entered password meets certain criteria
    """
    passwd = input('Enter a password to verify: ')
    flag = 0
    while True:
        if (len(passwd))<8:
            flag = -1
            break
        elif not re.search('[a-z]', passwd):
            flag = -1
            break
        elif not re.search('[A-Z]', passwd):
            flag = -1
            break
        elif not re.search("[_@$]", passwd): 
            flag = -1
            break
        elif not re.search('[1-9]', passwd):
            flag = -1
            break
        else:
            flag = 0
            print('Valid Password')
            break
    if flag == -1:
        print('Invalid password')

# passwd_checker()

min_uppercase, min_lowercase, min_punctuation, min_digits = 0, 0, 0, 0
password = input('Enter a password to verify: ')
if len(password) >= 8:
    for item in password:
        if (item.islower()):
            min_lowercase+=1
        if (item.isupper()):
            min_uppercase+=1
        if (item.isdigit()):
            min_digits+=1
        if (item=='@'or item=='$' or item=='_'):
            min_punctuation+=1
    if (min_lowercase>2 and min_uppercase>2 and min_digits>1 and min_punctuation>1):
        print('Valid password')
    else:
        print('Invalid password. Try again')

