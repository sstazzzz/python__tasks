# coding=windows-1251
# ������� 1
print("����")
num = int(input("������� ����� �����:"))
if num == 0:
    print("������� �����")
else:
    add_str = ""
    if num > 0:
        sign = "�������������"
    else:
        sign = "�������������"
    if num % 2 == 1:
        parity = "��������"
        add_str = "����� �� �������� ������"
    else:
        parity = "������"
    print(f"{sign} {parity} �����")
    if add_str != "":
        print(add_str)
        
# ������� 2
print("������� ����� ���������� ���������� �������")
word = input()
letter_a = word.count("a")
letter_e = word.count("e")
letter_i = word.count("i")
letter_o = word.count("o")
letter_u = word.count("u")
vowels = letter_a+letter_e+letter_i+letter_o+letter_i
consonants = len(word) - vowels 
print(f"��������� {consonants} ����.")
print(f"������� {vowels} ����.")
print("���������� ������� ����")
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


# ������� 3
print("������� ����������� ����� ���������� � �������:")
min_sum_startup = int(input())
print("������� ����� ������:")
mike_sum = int(input())
print("������� ����� �����:")
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














