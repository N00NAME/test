class Cat:

    def __init__(self, name):
        self.name = name
        self.meal = 30
        self.home = None

    def __str__(self):
        return ('{} - сытость: {} \tдом: {}'.format(self.name, self.meal, self.home))


Kimbo = Cat('Kimbo')
print(Kimbo)
