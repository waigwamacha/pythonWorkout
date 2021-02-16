
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
            if len(self.scoops) < Bowl.max_bowls:
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

twenty = Transaction()
twenty.new_transaction(10, -100, -50, 350)


