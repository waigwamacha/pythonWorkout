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

def sum_numbers():
    thisinp = '10 abc 20 de44 30 55fg 40'.split()
    for value in thisinp:
        if value.isdigit():
            print(value)  ##how to sum these

sum_numbers()