import time


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
            print(f'\t self.index {self.index} is too big. Exiting')
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

for index, letter in enumerate('abc'):
    print(f'{index}: {letter}')
    print(time.perf_counter())

class MyEnumerate():
    """
    class that works like the built-in enumerate function 
    """ 
    
