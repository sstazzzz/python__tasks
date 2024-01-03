# coding=windows-1251
import random

# Задание 1

def create_matrix(rows, columns):
    A = []
    for i in range(rows):
        line = []
        for j in range(columns):
            line.append(random.randint(-200,200))
        A.append(line)
    return A

def sum_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Нельзя сложить матрицы разной размерности.")
        return
    C = []
    for i in range(len(A)):
        line = []
        for j in range(len(A[0])):
            line.append(A[i][j] + B[i][j])
        C.append(line)
    return C

def print_matrix(A):
    for i in range(len(A)):
        print(A[i])
            
random.seed()
print("Введите размерность матрицы в формате rows:columns ")
rows, columns = map(int, input().split(":"))
A = create_matrix(rows, columns)
print("Матрица А:")
print_matrix(A)
B = create_matrix(rows, columns)
print("Матрица В:")
print_matrix(B)
C = sum_matrix(A, B)
print("Матрица С = А+В:")
print_matrix(C)
