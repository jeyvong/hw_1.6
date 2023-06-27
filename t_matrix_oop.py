#!/usr/bin/python3

class PrintMatrix:
    def __init__(self, matrix, rem):
        self.__matrix = matrix
        self.__rem = rem
        print(f"{rem}")
        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

class InputMatrix:
    def __init__(self):
        self.matrix = []

    def input_matrix(self):
        matrix_size_m = int(input("Размер матрицы m-строк:"))
        matrix_size_n = int(input("Размер матрицы n-столбцов:"))

        for i in range(1, matrix_size_m + 1):
            a = []
            for j in range(1, matrix_size_n + 1):
                matrix_cur = int(input(f"укажите А(m{i},n{j}):"))
                a.append(matrix_cur)
            self.matrix.append(a)
    def rem_matrix(self):
        rem = "Исходная матрица:"
        return rem


class TransponMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpon_matrix(self):
        matrixB = []
        for i in range(len(self.matrix[0])):
            b = []
            for j in range(len(self.matrix)):
                b.append(self.matrix[j][i])
            matrixB.append(b)
        return matrixB
    def rem_matrix(self):
        rem = "Транспонированная матрица:"
        return rem


input_matrix = InputMatrix()
input_matrix.input_matrix()

transpon_matrix = TransponMatrix(input_matrix.matrix)

printMatrix1 = PrintMatrix(input_matrix.matrix, input_matrix.rem_matrix())
printMatrix2 = PrintMatrix(transpon_matrix.transpon_matrix(), transpon_matrix.rem_matrix())
