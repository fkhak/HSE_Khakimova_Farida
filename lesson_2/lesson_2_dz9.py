#1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив,
# содержащий отсортированные числа от 10 до 250 млн.

#Можно использовать функцию randomint из модуля random для ещё большей рандомизации значений,
# но для целей работы алгоритма бинарного поиска проследите,
# чтобы значения в массиве были отсортированы.

#2. Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.

#3. Напишите функцию для алгоритма линейного поиска.

#4. Напишите функцию для алгоритма бинарного поиска.

#5. Проверьте наличие ранее сгенерированных случайных чисел в массиве
# с помощью алгоритмов линейного и бинарного поиска, замерьте время

import random
import time
from typing import List, Optional


def generate_sorted_array(start: int, end: int) -> List[int]:
    """Генерация отсортированного массива со случайным шагом от 3 до 5"""
    step = random.randint(3, 5)
    return list(range(start, end + 1, step))


def generate_random_numbers(count: int, min_val: int, max_val: int) -> List[int]:
    """Генерация случайных чисел в заданном диапазоне"""
    return [random.randint(min_val, max_val) for _ in range(count)]


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Алгоритм линейного поиска"""
    for i, num in enumerate(arr):
        if num == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Алгоритм бинарного поиска"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def measure_search_time(search_func, arr: List[int], targets: List[int]) -> float:
    """Измерение времени выполнения поиска"""
    start_time = time.time()

    for target in targets:
        search_func(arr, target)

    return time.time() - start_time


def main():
    # Параметры генерации
    START = 10
    END = 250000000
    RANDOM_NUMBERS_COUNT = 10

    # Генерация данных
    print("Генерация отсортированного массива...")
    sorted_array = generate_sorted_array(START, END)

    print("Генерация случайных чисел...")
    random_numbers = generate_random_numbers(RANDOM_NUMBERS_COUNT, START, END)

    # Проверка работы алгоритмов
    print("\nПроверка работы алгоритмов поиска:")

    # Линейный поиск
    linear_time = measure_search_time(linear_search, sorted_array, random_numbers)
    print(f"Время линейного поиска: {linear_time:.4f} секунд")

    # Бинарный поиск
    binary_time = measure_search_time(binary_search, sorted_array, random_numbers)
    print(f"Время бинарного поиска: {binary_time:.4f} секунд")

    # Сравнение эффективности
    speedup = linear_time / binary_time if binary_time > 0 else float('inf')
    print(f"Бинарный поиск быстрее в {speedup:.1f} раз")

    # Демонстрация корректности работы
    print("\nДемонстрация поиска для первых 5 чисел:")
    for i, target in enumerate(random_numbers[:5]):
        linear_result = linear_search(sorted_array, target)
        binary_result = binary_search(sorted_array, target)

        print(f"Число {target}: линейный поиск -> {linear_result}, бинарный поиск -> {binary_result}")


if __name__ == "__main__":
    main()
