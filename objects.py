
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
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for scoop in new_scoops:
            self.scoops.append(scoop)
        # print(self.scoops)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('persimmon')

# b = Bowl()
# b.add_scoops(s1, s2, s3)
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
    def __init__(self):
        self.shelf = []

    def add_books(self, *books):
        for book in books:
            self.shelf.append(book)

    def total_price(self):
        total_prices = 0
        for book in self.shelf:
            total_prices += float(book.price)
        return total_prices

book1 = Book('Chelkash', 'Maxim Gorky', '23.99')
book2 = Book('Vanka', 'Chekhov', '13.99')

fiction = Shelf()
fiction.add_books(book1, book2)
print(fiction.total_price())




