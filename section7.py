# Анализ текста. Популярность.
text = "hello word of word"
chars_popularity = {}
words_popularity = {}


# Римские цифры
arabic_num = 3999;
rom_num = {0: '', 1: 'I',2: 'II',3: 'III',4: 'IV', 5: 'V',6:'VI',8:'VIII', 9: 'IX', 
          10: 'X',20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',60: 'LX',70:'LXX',80:'LXX',90:'XC', 
          100: 'C',200:'CC',300:'CCC', 400: 'CD', 500: 'D',600: 'DC',700: 'DCC',800:'DCCC', 900: 'CM', 
          1000: 'M',2000:'MMM',3000:'MMM'}

thousand = arabic_num // 1000
hundred = arabic_num // 100 % 10
ten = arabic_num // 10 % 10
ones = arabic_num % 10

if arabic_num >= 1 and arabic_num <= 3999:
    if thousand == 0:
        print(rom_num.get(hundred*100),rom_num.get(ten*10),rom_num.get(ones))
    elif hundred == 0:
        print(rom_num.get(ten*10),rom_num.get(ones))
    elif ten == 0:
        print(rom_num.get(ones))
    elif thousand != 0:
        print(rom_num.get(thousand*1000),rom_num.get(hundred*100),rom_num.get(ten*10),rom_num.get(ones))
else:
    print("Wrong Data")


# Ленивый спекулянт
rates = {'Sberbank': 55.8, 'VTB24': 53.91}
min_value = min(rates.values())

for key,value in rates.items():
    if value == min_value:
        print(key,"->",value)

# Вверх дном
book = {'Petr': '546810', 'Katya': '241815'}
book_reverse = {}

for key,value in book.items():
    book_reverse[value] = key
print(book_reverse)

# Структурируем данные
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]

rate_dict = dict(zip(dates, rates))
print(rate_dict)