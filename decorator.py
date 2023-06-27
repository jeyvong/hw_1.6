def matrix_output(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def input_matrix():
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
    matrix_output(matrixA)

    return matrixA


def transpon_matrix(matrixA):
    matrixB = []
    for i in range(len(matrixA[0])):
        b = []
        for j in range(len(matrixA)):
            b.append(matrixA[j][i])
        matrixB.append(b)

    print("Транспонированная матрица:")
    return matrixB


matrixA = input_matrix()
matrixB = transpon_matrix(matrixA)
matrix_output(matrixB)
