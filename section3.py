
#1. Welcome to Python
name = "Dmitry Shchegolev"
print(f"Hello {name}! You just delved into Python. Great start!")

#2. Python art
thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))  



#3. Заголовок
text = "hello world"
print(text.title())


#4. Форматированный вывод денежной суммы
amount = 100500.157
print('{0:,.2f}'.format(abs(amount)))

#5. Дизайнер ковриков
height = 11
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('WELCOME'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))

#6. Произведение цифр
value = 123405
product = 1
while value != 0:
    temp = value % 10
    if temp == 0:
        value = value // 10
    else:
        product *= temp
        value = value // 10
print("PROD: ",  product)