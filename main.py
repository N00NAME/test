class Cat:
    def __init__(self, name):
        self.name = name
        self.meal = 30
        self.home = None

    def __str__(self):
        return '{} - сытость: {} \tдом: {}'.format(self.name, self.meal, self.home)


class Home:
    def __init__(self, name):
        self.name = name
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


class Human:
    def __init__(self, name):
        self.name = name
        self.hunger = 30
        self.home = None

    def __str__(self):
        return '{} живет в {} - сытость: {} '.format(self.name, self.home, self.hunger)

    def go_home(self, home):
        self.home = home.name
        home.dirty = False
        print('{} вьехал в дом {}'.format(self.name, self.home))

    def get_cat(self, cat, home):
        cat.home = home.name
        home.bowl = 20
        home.dirty = True


my_home = Home(name='My')
print('Построили дом')
print(my_home)

Bill = Human(name='Bill')
print('Создали человека')
print(Bill)

Bill.go_home(home=my_home)
print(Bill)
print(my_home)
print('------------------------------')

Kimbo = Cat(name='Kimbo')
print('Родился кот')
print(Kimbo)

Bill.get_cat(cat=Kimbo, home=my_home)
print('Поселили {} в дом {}'.format(Kimbo.name, my_home.name))
print(my_home)
