# coding=windows-1251

# ������� 1 
print("������� ��� ������ �������:")
type = input()
print("������� ������� �������:")
age = int(input())
print("������� ������ �������:")
name = input()

remainder = age % 10
if remainder == 1:
    year = "���."
elif remainder >1 and remainder < 5:
    year = "����."
else:
    year = "���."
print(f"��� {type} �� ������ \"{name}\". �������: {age} {year}")


# ������� 2
# �������������, ������� ������, ������� ������������, ������������, ������� �������� (Homo sapiens)
print("������� 5 ������ ����� �������� �������� (������������), ���������� � ������� enter")
for i in range(5):
    if i == 0:
        print("1 ������")
        a = input()
    elif i == 1:
        print("2 ������")
        b = input()
    elif i == 2:
        print("3 ������")
        c = input()
    elif i == 3:
        print("4 ������")
        d = input()
    elif i == 4:
        print("5 ������")
        e = input()        
print(a, b, c, d, e, sep="=>")
