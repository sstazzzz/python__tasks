# coding=windows-1251

# ������� 1
print("������� ���������� �����:")
count_n = int(input())
list_array = []
print("������ ������� ���� �����:")
for i in range(count_n):
    list_array.append(int(input()))
list_array.reverse()
print(*list_array)


# ������� 2
print("������� ���������� �����:")
count_n = int(input())
list_array = []
print("������ ������� ���� �����:")
for i in range(count_n):
    list_array.append(int(input()))
list_array.insert(0, list_array.pop())   
print(*list_array)


# ������� 3
print("������� ������������ ����� ��� ����� �����:")
weight = int(input())
print("������� ���������� �������:")
n = int(input())
list_array = []
for i in range(n):
    print(f"������� ����� ������ {i}, ������� �� ��������� ��� ����� {weight}")
    list_array.append(int(input()))
list_array.sort()
counter = 0
while len(list_array)>1:
    counter += 1
    if list_array[-1] + list_array[0] <= weight:
        print(f"����� {counter}: {list_array.pop()} {list_array[0]}")
        del list_array[0]
    else:
        print(f"����� {counter}: {list_array.pop()}")
if len(list_array) == 1:
    counter += 1
    print(f"����� {counter}: {list_array.pop()}")
