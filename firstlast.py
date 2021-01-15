
import operator 
from collections import Counter

def firstlast(element1):
    """[summary]

    Args:
        element1 ([type]): takes in an swequence(string, tuple, or list) and returns the first and last elements
    """
    elemt1 = element1[:0]+ element1[-1:] #we use slices here
    print(elemt1)

# firstlast('a good boy')

def even_odd_sums(nums, n):
    """takes a lsit or tuple and returns the sum of even-indexed numbers and odd-indexed numbers
    """
    # maxvalue = int(input("Please enter the max value: "))
    even_nums = 0
    odd_nums = 0
    final = []
    for num in range(n+1):
        if num % 2 == 0:
            even_nums += nums[num]
        else:
            odd_nums += nums[num]
    final.append(even_nums)
    final.append(odd_nums)
    print(final)

# even_odd_sums([10, 20, 30,40,50,60], 5)

def plus_minus(nums, n):
    """takes a lsit or tuple and returns altenate sum and minus of numbers
    """
    total_sum = 0
    for num in range(n+1):
        if num % 2==0:
            total_sum += nums[num]
        else:
            total_sum += nums[num]
    print(total_sum)

# plus_minus([10, 20, 30,40,50,60], 5)

PEOPLE = [
    {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'}, 
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'} 
    ]

def alphabetize_names(list_of_dicts):
    """Sort disctionaries by first name then by last name"""
    # return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

    # for person in people:
    #     print(f'{person["last"]}, {person["first"]}, {person["email"]}')
    for person in sorted(list_of_dicts, key=operator.itemgetter('last', 'first')):
        print(f'{person["last"]}, {person["first"]}, {person["email"]}')
    
# alphabetize_names(PEOPLE)
