n, m = map(int, input().split())

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

cost_table = []
for _ in range(n):
    cost_table.append([0] * m)

cost_table[0][0] = grid[0][0]

for j in range(1, m):
    cost_table[0][j] = cost_table[0][j-1] + grid[0][j]

for i in range(1, n):
    cost_table[i][0] = cost_table[i-1][0] + grid[i][0]

for i in range(1, n):
    for j in range(1, m):
        cheaper_put = min(cost_table[i-1][j], cost_table[i][j-1])
        cost_table[i][j] = cheaper_put + grid[i][j]

print(cost_table[n-1][m-1])