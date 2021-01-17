a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]


class MatrixClass:
    """ Принимает данные (список списков) для формирования матрицы """

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        """ Вывод матриц в привычном виде """
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        """ Реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
        новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
        матрицы складываем с первым элементом первой строки второй матрицы и т.д. """
        c = []
        for i in range(len(self.lists)):
            c.append([])
            # print(c)
            for j in range(4):

                c[i].append((self.lists[i][j]) + other.lists[i][j])
        return "\n".join(map(str, c))
        # return c


matrix1 = MatrixClass(a)
matrix2 = MatrixClass(b)
print(f"matrix 1:\n{matrix1}")
print(f"matrix 2:\n{matrix2}")
print(f"matrix 1+matrix2:\n{matrix1 + matrix2}")
