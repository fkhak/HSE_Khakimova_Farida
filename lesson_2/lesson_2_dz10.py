#1. Сгенерируйте массив из целых чисел, содержащий 100 000 элементов, с помощью функции randomint из модуля random.

#2. Сгенерируйте с помощью функции range массив, содержащий словари со следующей структурой:

#{
#	“num_1”: randomint(1,1_000_000),
#	“num_2”: randomint(1,1_000_000)
#}

#Длина массива должна составлять 100 000 элементов.

#3. Напишите функцию алгоритма сортировки пузырьком и с её помощью отсортируйте первый массив.

#4. Отсортируйте второй массив с помощью встроенного спиского метода .sort()
# и лямбда-функции сначала по первому ключу, потом по второму

import random
import time
from typing import List, Dict


def generate_random_numbers(count: int, min_val: int, max_val: int) -> List[int]:
    """Генерация массива случайных чисел"""
    return [random.randint(min_val, max_val) for _ in range(count)]


def generate_dict_array(count: int, min_val: int, max_val: int) -> List[Dict]:
    """Генерация массива словарей"""
    return [
        {"num_1": random.randint(min_val, max_val),
         "num_2": random.randint(min_val, max_val)}
        for _ in range(count)
    ]


def bubble_sort(arr: List[int]) -> List[int]:
    """Алгоритм сортировки пузырьком"""
    n = len(arr)
    # Создаем копию массива, чтобы не изменять оригинал
    sorted_arr = arr.copy()

    for i in range(n):
        # Флаг для оптимизации - если не было обменов, массив отсортирован
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Обмен элементов
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True

        # Если не было обменов, выходим досрочно
        if not swapped:
            break

    return sorted_arr


def main():
    # Параметры генерации
    COUNT = 100000
    MIN_VAL = 1
    MAX_VAL = 1000000

    print("Генерация массивов...")

    # 1. Генерация массива чисел
    numbers_array = generate_random_numbers(COUNT, MIN_VAL, MAX_VAL)

    # 2. Генерация массива словарей
    dict_array = generate_dict_array(COUNT, MIN_VAL, MAX_VAL)

    # 3. Сортировка пузырьком
    print("Сортировка пузырьком...")
    start_time = time.time()
    sorted_numbers = bubble_sort(numbers_array)
    bubble_sort_time = time.time() - start_time
    print(f"Время сортировки пузырьком: {bubble_sort_time:.2f} секунд")

    # 4. Сортировка словарей с помощью .sort() и лямбда-функции
    print("Сортировка массива словарей...")

    # Создаем копию для сортировки
    dict_array_copy = dict_array.copy()

    start_time = time.time()
    # Сортировка сначала по num_1, затем по num_2
    dict_array_copy.sort(key=lambda x: (x["num_1"], x["num_2"]))
    dict_sort_time = time.time() - start_time
    print(f"Время сортировки словарей: {dict_sort_time:.4f} секунд")

    # Проверка корректности сортировки
    print("\nПроверка корректности сортировки:")

    # Проверка сортировки чисел
    is_numbers_sorted = all(sorted_numbers[i] <= sorted_numbers[i + 1]
                            for i in range(len(sorted_numbers) - 1))
    print(f"Числовой массив отсортирован корректно: {is_numbers_sorted}")

    # Проверка сортировки словарей
    is_dict_sorted = all(
        (dict_array_copy[i]["num_1"] < dict_array_copy[i + 1]["num_1"] or
         (dict_array_copy[i]["num_1"] == dict_array_copy[i + 1]["num_1"] and
          dict_array_copy[i]["num_2"] <= dict_array_copy[i + 1]["num_2"]))
        for i in range(len(dict_array_copy) - 1)
    )
    print(f"Массив словарей отсортирован корректно: {is_dict_sorted}")

    # Вывод первых 5 элементов для демонстрации
    print("\nПервые 5 элементов отсортированного числового массива:")
    print(sorted_numbers[:5])

    print("\nПервые 5 элементов отсортированного массива словарей:")
    for item in dict_array_copy[:5]:
        print(item)


if __name__ == "__main__":
    main()