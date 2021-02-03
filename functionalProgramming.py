import operator 

empty_l = []
for i in range(15):
    i = str(i)
    empty_l.append(i)
empty_l = ','.join(empty_l)
# print(empty_l)

# [str(i) ','.join(i) for i in range(15)]
new_list = [''.join(str(i)) 
            for i in range(15)]
# print(new_list)
even_odd = [(x, y)
            for x in range(5)
            if x % 2
            for y in range(5)
            if y % 3]

# print(even_odd)

all_places = {'USA': ['Philadelphia', 'New York', 'Cleveland', 'San Jose', 'San Francisco'],
'China': ['Beijing', 'Shanghai', 'Guangzhou'], 'UK': ['London'],
'India': ['Hyderabad']}

cities = [one_city
            for country, cities in all_places.items()
            for one_city in cities]
# print(cities)
country_city = [(city, country)
                for country, cities in sorted(all_places.items())
                for city in cities]
# print(country_city)

some_list = [''.join(str(i)) 
            for i in range(15)
            if i > 0 and i < 10]

# print(some_list)

sum(x*x for x in range(1000)) #generator

added = sum(number 
        for number in range(200))
# print(added)
thistxt = ['abc def', 'ghi jkl']

reverse_words = [i[::-1] for i in thistxt]
# print(reverse_words)

words = 'this is a bunch of words'.split()
x = map(len, words)
# print(sum(x))

def is_a_long_word(one_word):
    return len(one_word) > 4

xy = filter(is_a_long_word, words)
# print(' '.join(xy))

letters = 'abdcefghi'
numbers = range(1, 5)
xyz = map(operator.mul, letters, numbers)
# print(' '.join(xyz))

# hexnums = '123 abc 1a2b 3f4e'
# print(sum([int(x, 16)
#     for x in hexnums.split()]))

# thisinp = '10 abc 20 de44 30 55fg 50'.split()
# print(sum([int(x) 
#         for x in thisinp
#         if x.isdigit()]))

def sum_numbers(numbers):
    return sum([int(number) 
        for number in numbers.split() 
        if number.isdigit()])

# print(sum_numbers(' a sd 34 12 67 90 pn'))

two_levels = [[1,2], [3,4]]
def flatten_list(multiple_lists):
    return [num
            for level in two_levels
            for num in level]


# print(flatten_list([[1,2], [3,4]]))
def flatten_odd_ints(mylists):
    return [elem
        for mylist in mylists
        for elems in mylist
        for elem in elems.split()
        if int(elem.isdigit())
        if elem/2 != 0]

print(flatten_odd_ints([['1 a c d 32 12'], ['a c 3r 54']]))

# many_levels = [['1 a c d 32 12'], ['a c 3r 54']]
# for level in many_levels:
#     for nums in level:
#         for num in nums.split():
#             # print(num)
#             if num.isdigit():
#                 num = int(num)
#                 if num/2 != 0:
#                     print(num)
