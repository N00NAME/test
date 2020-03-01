class Cat:

    def __init__(self, name):
        self.name = name
        self.meal = 30
        self.home = None

    def __str__(self):
        return '{} - сытость: {} \tдом: {}'.format(self.name, self.meal, self.home)


Kimbo = Cat('Kimbo')
print(Kimbo)


class Home:
    def __init__(self):
        self.bowl = None
        self.dirty = False
        self.meal = 50
        self.money = 100

    def __str__(self):
        if self.dirty:
            dirt = 'грязно'
        else:
            dirt = 'чисто'
        return 'В доме {}, корма: {}, еды: {}, денег: {}'.format(dirt, self.bowl, self.meal, self.money)


sweet_home = Home()
print(sweet_home)
