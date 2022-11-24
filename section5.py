#1. Fizz Buzz
x = int(input("Enter X: "))
divide = ("Fizz Buzz" if x % 3 == 0 and x % 5 == 0 else 
    "Fizz" if x % 3 == 0 else 
    "Buzz" if x % 5 == 0 else 
    str(x)
    )
print("Результат: ", divide)

#1. Fizz Buzz
X = int(input("Enter X: "))
if X % 3 == 0 and X % 5 == 0:
    print("результат: Fizz Buzz")
elif X % 3 == 0:
    print("результат: Fizz")
elif X % 5 == 0: 
    print ("результат: Buzz")
else:
    print("результат: ", X)

# 2. Оценка числа
value = int(input("Enter X: "))
if value % 2 != 0:
    print("результат: Плохо")
elif ((value > 2 and value < 5) and value % 2 == 0):
    print("результат: Неплохо")
elif ((value > 6 and value < 20) and value % 2 == 0):
    print("результат: Так себе")
elif value > 20:
    print("результат: Отлично")

#3. Последовательность
n = int(input("Enter N: "))
for i in range(n):
    print(i + 1 , end = "")

#4. Секретное сообщение
string = "How are you? Eh, ok. Low or Lower? Ohhh."
txt = ''
for x in string:
    if x.isupper():
        txt += x
print("\n"+ txt)

#5. Три слова
text = "start 5 one two three 7 end"