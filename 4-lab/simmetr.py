n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

is_symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break # Если нашли несовпадение, дальше можно не искать

if is_symmetric:
    print("YES")
else:
    print("NO")