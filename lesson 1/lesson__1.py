# Задание 1
# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# а затем выведите на экран.
# Используйте функции для консольного ввода input() и консольного вывода print().

# Попробуйте также через встроенную функцию id() понаблюдать,
# какие типы объектов могут изменяться и сохранять за собой адрес в оперативной памяти.


name = "Иван"
age = 25
is_student = True

print("Имя:", name)
print("Возраст:", age)
print("Студент:", is_student)

user_name = input("Введите ваше имя: ")
user_age = int(input("Введите возраст: "))


print("Тип user_name:", type(user_name))
print("Тип user_age:", type(user_age))

x = 10
print("id(x):", id(x))
x = 20
print("id(x):", id(x))


list_example = [1, 2, 3]
print("id(list_example):", id(list_example))
list_example.append(4)
print("id(list_example):", id(list_example))

# Задание 2
# Пользователь вводит время в секундах.
# Рассчитайте время и сохраните отдельно в каждую переменную количество часов,
# минут и секунд. Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
#
# Используйте приведение типов для перевода строк в числовые типы.
# Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit().
#
# Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.

seconds_input = input("Введите время в секундах: ")
if not seconds_input.isdigit():
    print("Ошибка: введите целое число!")
else:
    total_seconds = int(seconds_input)
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

hours_str = str(hours)
minutes_str = str(minutes)
seconds_str = str(seconds)

print("Часы:", hours_str)
print("Минуты:", minutes_str)
print("Секунды:", seconds_str)

# Задание 3
#Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.

# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Выведите данные в консоль.

n = input("Введите число от 1 до 9: ")

if not n.isdigit() or int(n) < 1 or int(n) > 9:
    print("Ошибка: введите число от 1 до 9!")
else:
    n_int = int(n)
    nn = int(n * 2)
    nnn = int(n * 3)
    total = n_int + nn + nnn

print(f"{n_int} + {nn} + {nnn} = {total}")