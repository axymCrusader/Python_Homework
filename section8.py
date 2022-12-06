"""
1. Не уникальные элементы.

Дано: непустой массив целых чисел.

Задание: нужно получить массив, состоящий только из неуникальных элементов данного массива. 

Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз).
Для решения этой задачи не меняйте оригинальный порядок элементов. Пример: [1, 2, 3, 1, 3], 
где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].

"""

elements = [10, 9, 10, 10, 9, 8]
elements_without_unique = [element for element in elements if elements.count(element) > 1]
print(f"{elements}, Результат: {elements_without_unique}")


"""
Дано: x, y, z, n.

Задание: нужно получить список всех возможных перестановок чисел x, y, z, где x + y + z != n.

"""



"""
Дано: n.

Задание: нужно получить список "удвоенных" нечетных чисел от 0 до n.

"""

n = 7
double_array = [element * 2 for element in range(n) if element % 2 != 0]
print(f"n = {n}, Результат: {double_array}")
