# coding=windows-1251

# ������� 1

pets = {}

name = input("������� ������ ������ �������:")
pets[name] = {}
pets[name]["��� �������"] = input("������� ��� ������ �������:")
pets[name]["������� �������"] = int(input("������� ������� �������:"))
pets[name]["��� ���������"] = input("������� ��� ���������:")

age = pets[name]["������� �������"]
remainder = age % 10
if remainder == 1:
    year = "���."
elif remainder >1 and remainder < 5:
    year = "����."
else:
    year = "���."

print(f"��� {pets[name]['��� �������']} �� ������ \"{name}\". ������� �������: {age} {year} ��� ���������: {pets[name]['��� ���������']} ")   


#������� 2

print("������� 2")
my_dict = {}
for i in range(10, -6, -1):
    my_dict[i] = i**i
print(my_dict)   