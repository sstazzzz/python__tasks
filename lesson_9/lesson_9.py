# coding=windows-1251

# �� ������� 1 � ������ ��� �������� �������.
# ������� 1 - 1 ������� �������
print("������� ���������� �����:")
count_n = int(input())
set_number = set()
print("������ ������� ���� �����:")
for i in range(count_n):
    set_number.add(int(input()))
print(f"� ���� ������ ����� {len(set_number)} ���������.")

# ������� 1 - 2 ������� �������
print("������� ����� ����� ������:")
s = set(input().split())
print(f"� ���� ������ ����� {len(s)} ���������.")


# ������� 2
print("������� ��� ������ ����� ����� ������:")
s1 = set(input().split())
s2 = set(input().split())
s2.intersection_update(s1)
print(f"����� ���������� � ���� �������: {len(s2)}")


# ������� 3
print("������� ������������������ ����� ����� ������:")
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
