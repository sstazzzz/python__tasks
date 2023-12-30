# coding=windows-1251
# Задание 1
print("Тест")
num = int(input("Введите целое число:"))
if num == 0:
    print("Нулевое число")
else:
    add_str = ""
    if num > 0:
        sign = "Положительное"
    else:
        sign = "Отрицательное"
    if num % 2 == 1:
        parity = "нечетное"
        add_str = "Число не является четным"
    else:
        parity = "четное"
    print(f"{sign} {parity} число")
    if add_str != "":
        print(add_str)
        
# Задание 2
print("Введите слово маленькими латинскими буквами")
word = input()
letter_a = word.count("a")
letter_e = word.count("e")
letter_i = word.count("i")
letter_o = word.count("o")
letter_u = word.count("u")
vowels = letter_a+letter_e+letter_i+letter_o+letter_i
consonants = len(word) - vowels 
print(f"Согласных {consonants} букв.")
print(f"Гласных {vowels} букв.")
print("Количество гласных букв")
if letter_a > 0:
    print("a", letter_a)
else:
    print("a - False")

if letter_e > 0:
    print("e", letter_e)
else:
    print("e - False")

if letter_i > 0:
    print("i", letter_i)
else:
    print("i - False")

if letter_o > 0:
    print("o", letter_o)
else:
    print("o - False")

if letter_u > 0:
    print("u", letter_u)
else:
    print("u - False")


# Задание 3
print("Введите минимальную сумму инвестиций в стартап:")
min_sum_startup = int(input())
print("Введите сумму Майкла:")
mike_sum = int(input())
print("Введите сумму Ивана:")
ivan_sum = int(input())
if mike_sum + ivan_sum < min_sum_startup:
    print(0)
elif mike_sum < min_sum_startup and ivan_sum < min_sum_startup:
    print(1)
elif mike_sum >= min_sum_startup and ivan_sum < min_sum_startup:
    print("Mike")
elif mike_sum < min_sum_startup and ivan_sum >= min_sum_startup:
    print("Ivan")
else:
    print(2)














