
class Scoop():
    """
    class that have a single attribute, flavor
    """
    def __init__(self, flavor):
        self.flavor = flavor

    def create_scoops():
        """
        creates three instances of the scoop class
        """
        scoops = [Scoop('vanilla'), Scoop('caramel'), Scoop('strawberry')]
        # scoops = [Scoop(flavor)
        #             for flavor in ('vanilla', 'caramel', 'strawberry')]
        for scoop in scoops:
            print(scoop.flavor)


# Scoop.create_scoops()

class Beverages():
    """ 
    class that has instances representing several beverages
    """ 
    def __init__(self, name, temp):
        self.name = name 
        self.temp = temp

    def create_beverage():
        beverages = [Beverages('IPA', 34.5), Beverages('IPA', 34.5)]

        for beverage in beverages:
            print(beverage.name, beverage.temp)

# Beverages.create_beverage()

class Bowl():
    """ 
    class of a bowl that accepts different ice cream flavors
    """ 
    max_bowls  = 3
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            if len(self.scoops) < self.max_bowls:
                self.scoops.append(scoop)
            # else:
            #     self.scoops.pop(-1)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')
# s4 = Scoop('caramel')
# s5 = Scoop('caramelli')

# b = Bowl()
# b.add_scoops(s1, s3, s2, s4, s5)
# print(b)

class BigBowl(Bowl):
    """ 
    child class of Bowl, but this accepts upto 5 bowls
    """
    max_bowls = 6

# b3 = BigBowl()
# b3.add_scoops(s1, s3, s2, s4, s5, s4)
# print(b3)

class Book():
    """ 
    class Book with title, author, price
    """ 
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price 
        
class Shelf():
    """ 
    shelf with books
    """ 
    num_books = 0
    def __init__(self):
        self.shelf = []

    def add_books(self, *books):
        for book in books:
            self.shelf.append(book)
        if books:
            Shelf.num_books = len(self.shelf)
            print(Shelf.num_books)

    def total_price(self):
        total_prices = 0
        for book in self.shelf:
            total_prices += float(book.price)
        return total_prices

book1 = Book('Chelkash', 'Maxim Gorky', '23.99')
book2 = Book('Vanka', 'Chekhov', '13.99')
book3 = Book('Vanka', 'Chekhov', '13.99')

# fiction = Shelf()
# fiction.add_books(book1, book2, book3)
# print(fiction.total_price())


class Person():
    """a class that creates a person"""
    def __init__(self, name):
        self.name = name

class Population():
    """
    a person class that has a population class attr that increases each time a person instance is created
    """
    population = 0
    def __init__(self):
        self.total_population = []

    def new_person(self, *people):
        "add a person to the total_population list"
        for one_person in people:
            self.total_population.append(one_person)
        if people:
            Shelf.population = len(self.total_population)
        print(Shelf.population)

        # def __repr__(self):
        #     return '/'.join(s for s in self.total_population)

# d1 = Person('kamau')
# d2 = Person('mwangi')
# # print(b1.name)
# c1 = Population()
# c1.new_person(d1, d2)

class Transaction():
    """
    class with instance representing a deposit or withdrawal from a bank account
    """ 
    current_balance = 0
    def __init__(self):
        self.total_amount = []

    def new_transaction(self, *transactions):
        for transaction in transactions:
            self.total_amount.append(transaction)
            Transaction.current_balance = sum(self.total_amount)
        print(Transaction.current_balance)

# twenty = Transaction()
# twenty.new_transaction(10, -100, -50, 350)

class Envelope():
    """ 
    envelope class with two attributes, weight(float) and was sent(Bool, default=False)
    """
    def __init__(self, weight, sent=False):
        self.weight = weight
        self.sent = sent
        self.total_postage = float(weight*10)

    def send(self):
        if self.total_postage >= float(self.weight*10):
            self.sent = True
            print(f'Postage was sent: {self.sent}')

    def postage_needed(self):
        needed = self.total_postage
        return f"We need postage of {needed}"

    def add_postage(self, new_postage):
        self.total_postage += new_postage
        return f'Postage added. Total: {self.total_postage}'

class BigEnvelope(Envelope):

    def __init__(self, weight):
        super().__init__(weight)
        self.total_postage = weight*15

    def postage_needed(self):
        needed = self.weight*15
        return f"We need postage of {needed}"

# d4 = Envelope(12)
# d4.send()
# print(d4.postage_needed())
# print(d4.add_postage(20))

# print(d4.add_postage(20))

class FlexibleDict(dict):
    """ 
    returns the key value pair irregardless of the key type.
    """ 
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self,key)
        

# d = FlexibleDict()
# d[1] = 100
# d['a'] = 350
# d['1'] = 650
# print(d)
# print(d['1'])

class StringKeyDict(dict):
    """ 
    changes the dictionary's keys into string type
    """ 
    def __getitem__(self, key):
        try:
            if key in self:
                key = str(key)
        except ValueError:
            pass
        return (self, key)

# fd = StringKeyDict()
# fd[1] = 30
# fd[2] = 40
# print(fd[2])
        

class Animal():
    """
    parent class for animals sheep, wolf, snakes and parrots
    """
    def __init__(self, sound, color, legs):
        self.species = self.__class__.__name__
        self.sound = sound
        self.color = color
        self.legs = legs

    def __repr__(self):
        return f'A {self.color} {self.sound}-{self.species} with {self.legs} legs'

# class ZeroLeggedAnimal(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)

# class Snake(ZeroLeggedAnimal):
#     def __init__(self, color):
#         super().__init__(color)

class Sheep(Animal):
    """
    child class of animal
    """
    def __init__(self, color):
        super().__init__('baa', color, 4)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__('woof', color, 4)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__('coo', color, 2)

sheep = Sheep('black')
wolf = Wolf('white')
parrot = Parrot('blue')
# print(sheep)
# print(parrot)
# print(sheep.species)

class AnimalLair():
    """
    a place for animals to live peacefully and safely 
    """
    num_animals = 0
    def __init__(self, id):
        self.id = id
        self.all_animals = []
    def add_animals(self, *animals):
        for animal in animals:
            self.all_animals.append(animal)
        # print(self.all_animals)
        if animals:
            AnimalLair.num_animals = len(self.all_animals)
        # print(AnimalLair.num_animals)
    def __repr__(self):
        output = f'Cage {self.id}:\n'
        output += '\n'.join('\t' + str(animal) for animal in self.all_animals)
        
        return output 


class Zoo():
    """
    Zoo that contains Animallairs for different animals 
    """
    def __init__(self, id):
        self.id = id
        self.lairs = []

    def add_lairs(self, *lairs):
        for lair in lairs:
            self.lairs.append(lair)

    def animals_by_color(self, *colors):
        return [animal
                for color in colors
                for lair in self.lairs
                for animal in lair.all_animals
                if animal.color == color]

    def animals_by_legs(self, num_legs):
        return [animal
                for lair in self.lairs 
                for animal in lair.all_animals
                if animal.legs == num_legs]

    def transfer_animal(self, target_zoo, transfer_animal):
        return [target_zoo.lair[0].append(animal)
                for lair in self.lairs
                for animal in lair.all_animals
                if animal == transfer_animal]


c1 = AnimalLair(1)
c2 = AnimalLair(2)
z = Zoo(1)
z2 = Zoo(2)
z.add_lairs(c1, c2)
z2.add_lairs(c2)
c1.add_animals(wolf, sheep, parrot)
c2.add_animals(sheep, wolf)
# print(c1)
# print(c2)
# print(z)
# print(z.animals_by_color('black', 'white'))
# print(z.animals_by_legs(2))
print(z.transfer_animal(z2, 'parrot'))

    





