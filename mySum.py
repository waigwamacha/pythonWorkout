def mysum(*numbers):
    """function that adds numbers together"""
    result = 0
    for number in numbers:
        result += number
    print(result)

mysum(1,2,3,5)
mysum(*[1,5,8])
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

mymean(2,4,6,8)