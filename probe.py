
# Вывод и форматирование


# name = input("Как вас зовут? ")
# print('Привет, {}!'.format(name))


# for i in 'Hello world!':
#     if i == ' ':
#         break
#     elif i == 'H':
#         continue
#     print(i * 2, end='')


# print(r'www.1st.com/download/version1_10')
# print(r'C:\temp\new')
# print('''\nМуха села
# # на варенье
# вот и все
# стихотворенье''')
# print("s \np \ta \nbbb")


# S = 'counter-terrorist'
# A = 'Andrew, Tony, Tomas'
# print(S.split('-'))
# print(A.split(','))
# print(S.upper())
# print(S.lower())
# print(S.capitalize())
# print(A.swapcase())


# coordinates = {'y': 10, 'x': 5}
# print('Coordinates: y={y}, x={x}'.format(**coordinates))


# print('{:<20}'.format('left aligned'))
# print('{:^20}'.format('center aligned'))
# print('{:>20}'.format('right aligned'))


# print('{:+f}; {:+f}'.format(3.14, -3.14))
# print('{: f}; {: f}'.format(3.14, -3.14))


# # % умножает число на 100!
# print('answers: {:.2%}'.format(8 / 11))

# Списки

# words = list('список')
# print(words)

# # пустой список
# s = []

# t = ['s', 'p', ['is', 'ok'], 2]
# print(t)

# c = [c + d for c in 'aeiy' if c != 'y' for d in 'bcdf' if d != 'd']
# print(c)

# c = [1, 'two', 123]
# c.append('new')
# print(c)

# # Расширяет список list, добавляя в конец все элементы списка L
# c = [1, [2, 3, 4], 5]
# L = ['six', 'seven', 'eight']
# c.extend(L)
# print(c)

# words = ['1', '2', '3']
# words.insert(1, 'вставка')
# print(words)

# words = ['a', 'b', 'c', 'd']
# print(words)
# words.remove('c')
# print(words)

# # Удаляет i-ый элемент и возвращает его. если не указать,удаляется последний элемент
# words = [1, 2, 3, 4, 5]
# print('список до удаления {}'.format(words))
# print('удалили из списка {}'.format(words.pop()))
# print('список после удаления {}'.format(words))
# N = 2
# print('Удалили из списка элемента {}  под индексом {}'.format(words.pop(N), N))

# # Поиск значения от 0 до длины списка, вывод его индекса
# c = ['1', '2', '3', '4']
# find_elemant = '3'
# print('Элемент {} найден под индексом '.format(find_elemant), end='')
# print(c.index(find_elemant, 0, len(c)))

# words = ['a', 'b', 'c', 'd', 'c', 'dc']
# print(words)
# print(words.count('c'))

# numbers = [3, 1, 5, 7, 2, 4, 6]
# print('список до сортировки {} '.format(numbers))
# numbers.sort()
# print('список после сортировки {} '.format(numbers))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# print('начальный список {} '.format(numbers))
# print('Отображение списка наоборот {} '.format(numbers[::-1]))
# print('Но исходный список не изменяется, лишь выводится {} '.format(numbers))

# numbers = [3, 1, 5, 7, 2, 4, 6]
# print('Начальный список {} '.format(numbers))
# numbers.reverse()
# print('После reverse список перевернут {} '.format(numbers))

# numbers = [3, 1, 5, 7, 2, 4, 6]
# print('Начальный список {} '.format(numbers))
# numbers.clear()
# print('Список после clear {} '.format(numbers))


# Таблица символов
# for code in range(127):
#     print(code, hex(code), chr(code))



# file = open('test.txt', mode='w', encoding='utf8')
# file.write('добавлено при создании')
# file.close()
#
# file = open('test.txt', mode='r', encoding='utf8')
# content = file.read()
# file.close()
# print(content)
#
# print('------------------')
#
# file = open('test.txt', mode='r+', encoding='utf8')
# content = file.read()
# file.write('\nДобавлено при второй записи')
# file.close()
#
# file = open('test.txt', mode='a', encoding='utf8')
# content = '\nДобавлено при третьей записи'
# file.write(content)
# file.close()
#
# file = open('test.txt', mode='r', encoding='utf8')
# copy_content = file.read()
# file.close()
# print(copy_content)
#
# file = open('copy_text.txt', mode='w', encoding='utf8')
# file.write(copy_content)
# file.close()
#
# file = open('copy_text.txt', mode='a', encoding='utf8')
# file.write('\nДобавлено')
# file.close()
#
# file = open('copy_text.txt', mode='r', encoding='utf8')
# content = file.read()
# file.close()
# print(content)
# with open('test.txt', mode='r+', encoding='utf8') as file:
#     for line in file:
#         print(line, end='')
# print('---------------')
# file = open('test.txt', mode='r+', encoding='utf8')
# lines = file.readlines()
# print(lines)
# file.close()
# for line in lines:
#     print(line, end='')
