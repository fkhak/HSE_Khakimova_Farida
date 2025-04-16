# Напишите функцию для валидации ИНН (идентификационного номера налогоплательщика),
# которая принимает в качестве аргумента строку, содержащую ИНН или просто набор цифр, похожий на ИНН.
#
# Функция возвращает True в случае, если ИНН прошёл проверку, и False, если проверка не пройдена.
#
# Для удобства лучше разбить код на несколько взаимосвязанных функций.

def validate_inn(inn_str):
    # Проверка на цифры и длину
    if not inn_str.isdigit():
        return False
    inn = list(map(int, inn_str))
    length = len(inn)
    if length not in (10, 12):
        return False

    # Проверка для 10-значного ИНН
    if length == 10:
        weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum = sum(w * inn[i] for i, w in enumerate(weights))
        control = checksum % 11
        if control > 9:
            control = control % 10
        return control == inn[9]

    # Проверка для 12-значного ИНН
    else:
        # Первое контрольное число
        weights1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum1 = sum(w * inn[i] for i, w in enumerate(weights1))
        control1 = checksum1 % 11
        if control1 > 9:
            control1 = control1 % 10

        # Второе контрольное число
        weights2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        checksum2 = sum(w * inn[i] for i, w in enumerate(weights2))
        control2 = checksum2 % 11
        if control2 > 9:
            control2 = control2 % 10

        return control1 == inn[10] and control2 == inn[11]

# Примеры вызовов функции
print("Проверка ИНН организации (10 цифр):")
print("7727563778 ->", validate_inn("7727563778"))
print("1234567890 ->", validate_inn("1234567890"))

print("\nПроверка ИНН физлица (12 цифр):")
print("500100732259 ->", validate_inn("500100732259"))
print("123456789012 ->", validate_inn("123456789012"))

# Пример с вводом данных от пользователя
inn_input = input("\nВведите ИНН для проверки: ")
print(f"Результат проверки: {validate_inn(inn_input)}")