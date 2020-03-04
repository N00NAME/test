class Cat:
    def __init__(self, name):
        self.name = name
        self.meal = 30
        self.home = None

    def __str__(self):
        return '{} - сытость: {}'.format(self.name, self.meal)

    def sleep(self):
        self.meal -= 10
        print('{} спал'.format(self.name))

    def eat(self):
        if self.home.bowl >= 10:
            self.meal += 20
            self.home.bowl -= 10
            print('{} поел'.format(self.name))
        else:
            print('{} нет корма'.format(self.name))

    def tear_wallpaper(self):
        self.meal -= 10
        self.home.dirty = True
        print('{} драл обои'.format(self.name))


class Home:
    def __init__(self, name):
        self.name = name
        self.bowl = 20
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
        self.hunger = 100
        self.home = None

    def __str__(self):
        return '{} - сытость: {} '.format(self.name, self.hunger)

    def go_home(self, home):
        self.home = home
        home.dirty = False
        print('{} въехал в дом {}'.format(self.name, self.home.name))

    def get_cat(self, cat, home):
        self.hunger -= 10
        cat.home = home
        home.bowl = 20
        home.dirty = True
        print('{} подобрал кота {} домой'.format(self.name, cat.name))

    def buy_cat_food(self):
        if self.home.money >= 30:
            self.home.bowl += 50
            self.home.money -= 30
            print('{} купил корм коту'.format(self.name))
        else:
            print('{} денег на корм нет'.format(self.name))

    def cleaning(self):
        self.home.dirty = False
        self.hunger -= 20
        print('{} Убрался дома'.format(self.name))

    def work(self):
        self.hunger -= 20
        self.home.money += 150
        print('{} сходил на работу'.format(self.name))

    def eat(self):
        if self.home.meal >= 50:
            self.hunger += 50
            self.home.meal -= 20
            print('{} поел'.format(self.name))
        else:
            print('{} нет еды'.format(self.name))

    def buy_food(self):
        if self.home.money >= 40:
            self.home.meal += 50
            self.home.money -= 40
            self.hunger -= 10
            print('{} сходил за едой'.format(self.name))
        else:
            print('{} деньги кончились'.format(self.name))


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

Bill.buy_cat_food()
print(my_home)

Bill.cleaning()
print(Bill)
print(my_home)

Bill.work()
print(Bill)
print(my_home)

Bill.eat()
print(Bill)
print(my_home)

print('-----------------------')
Kimbo.sleep()
print(Kimbo)
Kimbo.tear_wallpaper()
print(Kimbo)
print(my_home)
Kimbo.eat()
print(Kimbo)
print(my_home)
