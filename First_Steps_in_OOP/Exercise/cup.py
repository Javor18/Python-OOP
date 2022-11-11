class Cup:

    def __init__(self, size, quantity):

        size -= quantity
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):

        if self.size - milliliters >= 0:

            self.size -= milliliters

    def status(self):

        return self.size

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())