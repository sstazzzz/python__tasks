# coding=windows-1251
# Задание 1
count_n = int(input("Сколько чисел вы будете вводить?"))
count_zero = 0
for i in range(count_n):
    a = int(input())
    if a == 0:
        count_zero += 1
print("Среди ваших чисел", count_zero, "равно нулю")    

# Задание 2
N = int(input("Введите натуральное число:"))
count = 0
for i in range(1, N+1):
    if N % i == 0:
        count += 1
print("Число", N, "имеет", count, "делителей")

# Задание 3
A, B = map(int, input("Введите числа A и B через пробел, где А <= B:").split())
for i in range(A, B+1):
    if i!=0 and i % 2 == 0:
        print(i, end = " ")
