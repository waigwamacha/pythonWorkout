import time
import os

class LoudIterator():

    def __init__(self, data):
        print('\tNow in __init__')
        self.data = data
        self.index = 0 #creates an index attr that keeps track of our current position

    def __iter__(self):
        print('\tNow in __iter__')
        return self

    def __next__(self):
        print('\tNow in next')
        if self.index >= len(self.data):
            # print(f'\t self.index {self.index} is too big. Exiting')
            raise StopIteration

        value = self.data[self.index]
        self.index += 1
        print(f'\tGot value {value}, incremented index to {self.index}')
        return value 

# for one_value in LoudIterator('abc'):
#     print(one_value)

def foo():
    yield 1
    yield 2
    yield 3

g = foo()
# for one_item in g:
#     print(one_item)

# for index, letter in enumerate('abc'):
#     print(f'{index}: {letter}')
    # print(time.perf_counter())

class MyEnumerate():
    """
    class that works like the built-in enumerate function 
    """ 
    def __init__(self, data):
        self.data = data 
        self.index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self.data == list(self.data) or str(self.data) or dict(self.data):
            pass

        if self.index >= len(self.data):
            raise StopIteration
        
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

# for index, letter in MyEnumerate(range(15)):
#     print(f'{index}: {letter}')

class MyNewEnumerate():
    """
    class that works like the built-in enumerate function 
    """ 
    def __init__(self, data):
        self.data = data 
        self.index = 0

    def __iter__(self):
        return MyEnumerateIterator(self.data)

class MyEnumerateIterator():
    """
    helper class for MyNewEnumerate 
    """
    def __init__(self, data):
        self.data = data 
        self.index = 0

    def __next__(self):
        if self.data == list(self.data) or str(self.data) or dict(self.data):
            pass

        if self.index >= len(self.data):
            raise StopIteration
        
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

# e = MyNewEnumerate('abc')
# print('\t*** A ***')
# for index, letter in e:
#     print(f'{index}: {letter}')
# print('\t*** B ***')
# for index, letter in e:
#     print(f'{index}: {letter}')
# print('\t*** C ***')
# for index, letter in e:
#     print(f'{index}: {letter}')

class Circle():
    """
    class that takes in a sequence and the number that defines the 
    number of times the elements will be displayed
    """
    def __init__(self, seq, num_times):
        self.seq = seq 
        self.num_times = num_times
        self.index = 0

    def __iter__(self):
        return CircleIterator(self.seq, self.num_times)

class CircleIterator():
    """
    helper class for the Circle class
    """
    def __init__(self, seq, num_times):
        self.seq = seq
        self.num_times = num_times
        self.index = 0

    def __next__(self):
        if self.index >= self.num_times:
            raise StopIteration
        
        values = (self.seq[self.index % len(self.seq)])
        self.index += 1
        return values
        
c =Circle('abcd', 20)
# print(list(c))


def read_all_filelines(dirname):
    """
    generator function to read all lines in files in a directory 
    """
    for filename in os.listdir(dirname):
        full_filename = os.path.join(dirname, filename)

        try:
            for line in open(filename):
                yield line
        except OSError:
            pass 

# for one_line in read_all_filelines('/Users/macbook/Documents/python/pythonWorkout/books/'):
#     print(one_line)


def timepassed(someiterable):
    """
    genetor that accepts an iterable argument and provides a tuple with time between operations and the next output
    """
    last_time = None
    for iterable in someiterable:
        current_time = time.perf_counter() #gets current time
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()

        yield (delta, iterable)


# for t in timepassed('abcdefg'):
#     print(t)
#     time.sleep(2)

def mychain(*data):
    """
    generator function that takes any number of arguments (iterables). calling it
    returns the next item from the current iterable, or the first elem from subsequent iterable
    """
    for iterable in data:
        for data in iterable:
            yield data

# e = mychain('abc', [1,2,3], {'a':1, 'b':2})
# for item in e:
#     print(item)

def myzip(arg1, arg2):
    """generator function that works like zip
    """
    for i in range(len(arg1)):
        yield f"{arg1[i]}, {arg2[i]}"

e = myzip('abc', [1,2,3])
for item in e:
    print(item)

