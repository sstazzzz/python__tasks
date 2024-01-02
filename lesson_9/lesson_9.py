# coding=windows-1251

# По Заданию 1 я сделал два варианта решения.
# Задание 1 - 1 вариант решения
print("Введите количество чисел:")
count_n = int(input())
set_number = set()
print("Теперь введите сами числа:")
for i in range(count_n):
    set_number.add(int(input()))
print(f"В этом наборе чисел {len(set_number)} различных.")

# Задание 1 - 2 вариант решения
print("Введите числа через пробел:")
s = set(input().split())
print(f"В этом наборе чисел {len(s)} различных.")


# Задание 2
print("Введите два списка чисел через пробел:")
s1 = set(input().split())
s2 = set(input().split())
s2.intersection_update(s1)
print(f"Чисел содержится в двух списках: {len(s2)}")


# Задание 3
print("Введите последовательность чисел через пробел:")
list_number = input().split()
set_number = set()
lenght = 0
for i in list_number:
    set_number.add(i)
    if len(set_number) > lenght:
        print("NO")
    else:
        print("YES")
    lenght = len(set_number)
