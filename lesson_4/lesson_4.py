# coding=windows-1251
# Задание 1
print("Введите стороны прямоугольника.")
print("Длина: ")
lenght= float(input())
print("Ширина: ")
wight= float(input())
print("Площадь прямоугольника равна", lenght*wight)
print("Периметр прямоугольника равен", (lenght+wight)*2)


# Задание 2
print("Введите 5-ти значное целое число.") 
a,b,c,d,e = map(int, input())
# десятки в степень
a1 = d**e
# умножаем на сотни 
a2 = a1*c
# делим на разность десятки тысяч и тысячи
total = a2/(a-b)
print(total)
