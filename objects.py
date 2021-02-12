
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


Scoop.create_scoops()