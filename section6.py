#1. Последний с четными
elements = []
sum_elements_even_index = 0 
if len(elements) != 0:
    for i,x in enumerate(elements):
        if i % 2 == 0:
            sum_elements_even_index += x
    print("результат: ", sum_elements_even_index * elements[-1]) 
else: 
    print("результат: 0")

#Max-min 
elements = [1, 2, 3]
max_element = max(elements)
min_element = min(elements)
print("результат: ", round(max_element - min_element, 3))


#Умная сортировка
elements = (-1, -2, -3, 0)
sorted_elements = sorted(elements, key = abs)
print("Результат: ", sorted_elements)

#Медиана
elements = [3, 6, 20, 99, 10, 1, 12, 7]
sorted_elements = sorted(elements)
len_elements = len(elements)

middle = len_elements // 2
left_element = middle - 1

if len_elements % 2 != 0:
    print("результат: ", sorted_elements[middle])
else:
    print("результат: ",(sorted_elements[left_element] + sorted_elements[middle]) / 2)
