# Создайте ряд функций для проведения математических вычислений:
#
# функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
# Принимает в качестве аргумента число, возвращает его факториал;
#
# поиск наибольшего числа из трёх.
# Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них;
#
# расчёт площади прямоугольного треугольника.
# Принимает в качестве аргумента размер двух катетов треугольника. Возвращает площадь треугольника.

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

def find_max(numbers: tuple) -> float:
    if len(numbers) != 3:
        raise ValueError("Кортеж должен содержать ровно три числа")
    return max(numbers)

print(find_max((3, 9, 5)))

def right_triangle_area(a: float, b: float) -> float:
    return 0.5 * a * b

print(right_triangle_area(3, 4))

# Создайте функцию для генерации текста с адресом суда.
#
# Функция должна по шаблону генерировать шапку для процессуальных документов
# с реквизитами сторон для отправки.
# Функция должна принимать в качестве аргумента словарь с данными ответчика и номером дела.

# На основании номера дела из списка судов должен быть выбран корректный суд для отправки.
# Данные по арбитражным судам есть в указанном выше файле. Используйте код суда из дела.
# С помощью f-string создайте шаблон для заполнения.
# В качестве истца укажите свои данные.
# В данные по ответчику подставьте данные, переданные в функцию в качестве аргумента.
# В конце шапки подставьте номер дела.
#
# Функция должна возвращать готовую шапку в виде строки.
#
# Создайте ещё одну функцию, которая принимает в себя список словарей с данными ответчика.
# Используйте цикл for для генерации всех возможных вариантов этой шапки
# с вызовом первой функции внутри тела цикла for и выводом данных, которые она возвращает в консоль.


from lesson_2_dzdata import respondents, courts

def generate_header(respondent, case_number,courts):
    # Извлекаем код суда из номера дела
    court_code = case_number.split('-')[0]

    # Ищем суд по коду
    selected_court = None
    for court in courts:
        if court['court_code'] == court_code:
            selected_court = court
            break

    if not selected_court:
        return "Суд не найден"

    # Данные истца
    plaintiff_data = {
        'full_name': 'Хакимова Фарида Фаритовна',
        'inn': '123456789012',
        'ogrn': '09876543210987',
        'address': '123456, г. Казань, ул. Пушкина, 10'
    }

    # Формируем шапку
    header = f"""
В {selected_court['court_name']}
Адрес: {selected_court['court_address']}

Истец: {plaintiff_data['full_name']}
ИНН {plaintiff_data['inn']} ОГРНИП {plaintiff_data['ogrn']}
Адрес: {plaintiff_data['address']}

Ответчик: {respondent['short_name']}
ИНН {respondent['inn']} ОГРН {respondent['ogrn']}
Адрес: {respondent['address']}

Номер дела {case_number}
    """
    return header.strip()

def generate_all_headers(respondents_list, courts_list):
    for respondent in respondents_list:
        case_number = respondent.get("case_number", "")
        header = generate_header(respondent, case_number, courts_list)
        print(header)
        print("-" * 50)

generate_all_headers(respondents, courts)