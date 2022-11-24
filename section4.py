from random import randint

#1. Среднее
print((randint(0, 100) + randint(0, 100) + randint(0, 100)) / 3)


#2. Деление и еще раз деление
x =  randint(0, 100)
y = randint(0, 100)
print (x // y ,",", x % y)

#3. Округление
x = 14.721
print('1) {:.2f}'.format(x))
print("2)", round(x))
print('3) {:011}'.format(x))

#4. Число "наоборот"
x = 123 
x_reverse = 0
while x != 0:
    temp = x % 10
    x_reverse = x_reverse * 10 + temp 
    x = x // 10
print(x_reverse)