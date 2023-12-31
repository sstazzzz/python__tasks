# coding=windows-1251

# Задание 1
print("Введите количество чисел:")
count_n = int(input())
list_array = []
print("Теперь введите сами числа:")
for i in range(count_n):
    list_array.append(int(input()))
list_array.reverse()
print(*list_array)


# Задание 2
print("Введите количество чисел:")
count_n = int(input())
list_array = []
print("Теперь введите сами числа:")
for i in range(count_n):
    list_array.append(int(input()))
list_array.insert(0, list_array.pop())   
print(*list_array)


# Задание 3
print("Введите максимальную массу для одной лодки:")
weight = int(input())
print("Введите количество рыбаков:")
n = int(input())
list_array = []
for i in range(n):
    print(f"Введите массу рыбака {i}, который не превышает вес лодки {weight}")
    list_array.append(int(input()))
list_array.sort()
counter = 0
while len(list_array)>1:
    counter += 1
    if list_array[-1] + list_array[0] <= weight:
        print(f"Лодка {counter}: {list_array.pop()} {list_array[0]}")
        del list_array[0]
    else:
        print(f"Лодка {counter}: {list_array.pop()}")
if len(list_array) == 1:
    counter += 1
    print(f"Лодка {counter}: {list_array.pop()}")
