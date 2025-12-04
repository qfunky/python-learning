n, m = map(int, input("Задать размеры массиву: ").split())

matrix = []
for _ in range(n):
    row = list(map(int, input("Элементы массива: ").split()))
    matrix.append(row)

i, j = map(int, input("Ввести номера столбцов: ").split())
i, j = i - 1, j - 1

for row_index in range(n):
    matrix[row_index][i], matrix[row_index][j] = matrix[row_index][j], matrix[row_index][i]

for row in matrix:
    print(*row)