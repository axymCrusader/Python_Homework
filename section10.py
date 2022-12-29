#1. Градусник
def convert_to_fahrenheit(value):
    return [(number * 9/5 + 32) for number in value]

#2. Длинномер.
def get_len_strings(text):
    return [len(char) for char in text] 

#3. Рефакторинг.
def get_d():
    return 0

#4. Возведение в степень.
def exponentiation(list_X, list_Y):
    exp_list = []
    for i,x in enumerate(list_X):
        exp_list.append(x ** list_Y[i])
    return exp_list

#5. Ленивая функция
def lazy_function(N):
    return 0

numers = [39.2, 36.5, 37.3, 37.8]
strings = ['Tina', 'Raj', 'Tom']
X = [2, 3, 4]
Y = [10, 11, 12]
N = 3

print(numers,"Результат:",convert_to_fahrenheit(numers))
print(strings,"Результат:",get_len_strings(strings))
print(f"X = {X}, Y = {Y}, Результат: {exponentiation(X,Y)}")
print(N,"Результат:",lazy_function(N))