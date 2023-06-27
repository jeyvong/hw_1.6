#!/usr/bin/python3
matrix_size_m = int(input("Размер матрицы m-строк:"))
matrix_size_n = int(input("Размер матрицы n-столбцов:"))

matrixA = []
for i in range(1, matrix_size_m + 1):
    a = []
    for j in range(1, matrix_size_n + 1):
        matrix_cur = int(input(f"укажите А(m{i},n{j}):"))
        a.append(matrix_cur)
    matrixA.append(a)

print("Исходная матрица:")
for row in matrixA:
    for element in row:
        print(element, end=" ")
    print()

#len(matrixA[0]) Количество столбцов
#len(matrixA) Количество строк

matrixB = []
for i in range(len(matrixA[0])):
    b = []
    for i in range(len(matrixA[0])):
        b = []
        for j in range(len(matrixA)):
            b.append(matrixA[j][i])
        matrixB.append(b)

print("Транспонированная матрица:")
for row in matrixB:
    for element in row:
        print(element, end=" ")
    print()