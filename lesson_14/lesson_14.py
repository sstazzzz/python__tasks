# coding=windows-1251


# Задание 1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_my_list(i):
    if i == len(my_list):
        print("Конец списка")
        return
    print(my_list[i], end = " ")
    print_my_list(i+1)
    
print_my_list(0)
