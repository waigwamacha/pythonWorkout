def mysum(*numbers):
    """function that adds numbers together"""
    result = 0
    for number in numbers:
        result += number
    print(result)

# mysum(1,2,3,5)
# mysum(*[1,5,8])
print('___*5')

def mymean(*numbers):
    """function that adds numbers together"""
    result = 0
    count = 0
    for number in numbers:
        result += number
        count += 1
    this_mean = result/count 
    print(this_mean)

# mymean(2,4,6,8)

def mysum_alltypes(*numbers):
    """function that adds numbers together"""
    if not numbers:
        return numbers
    output = numbers[0]
    for number in numbers[1:]:
        output += number
    print(output)

# mysum_alltypes('a')
# mysum_alltypes('a', 'b', 'c', 'd')
# mysum_alltypes(10,20,30,40,50)

def sum_numeric(*numbers):
    """function that adds numbers together"""
    if not numbers:
        return numbers
    output = numbers[0]
    for number in numbers[1:]:
        if type(number) == int:
            output += number
    print(output)

# sum_numeric(10, 20, 'a', '30', 'bcd')

def sum_five_three():
    output = 0
    for number in range(1000):
        if number % 3 and number % 5:
            output += number
    print(output)

sum_five_three()