# 1. Список из числа.
def Get_list_reverse_number(number):
    numbers_list = []
    while(number != 0):
        temp = number % 10
        numbers_list.append(temp)
        number = number // 10
    return numbers_list


#2. Палиндром.
def is_polydrome_v1(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    return False

def is_polydrome_v2(string):
    return string == "".join(reversed(string))


#3. Деканат.
def get_student_list(dekan_list):

    return 0


value = 12
print(value, "Результат: ",Get_list_reverse_number(value))

text = "lol"
print(text, "Результат: ",is_polydrome_v2(text))