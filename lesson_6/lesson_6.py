# coding=windows-1251
# ������� 1
count_n = int(input("������� ����� �� ������ �������?"))
count_zero = 0
for i in range(count_n):
    a = int(input())
    if a == 0:
        count_zero += 1
print("����� ����� �����", count_zero, "����� ����")    

# ������� 2
N = int(input("������� ����������� �����:"))
count = 0
for i in range(1, N+1):
    if N % i == 0:
        count += 1
print("�����", N, "�����", count, "���������")

# ������� 3
A, B = map(int, input("������� ����� A � B ����� ������, ��� � <= B:").split())
for i in range(A, B+1):
    if i!=0 and i % 2 == 0:
        print(i, end = " ")
