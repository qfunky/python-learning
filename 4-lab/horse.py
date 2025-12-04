pos_x, pos_y = map(int, input().split())

x = pos_x - 1 # Приколы с кордами чтобы совпало с индексами питона
y = pos_y - 1

board = []
for i in range(8):
    row = ['.'] * 8
    board.append(row)

board[x][y] = 'K'

moves = [
    (-2, -1), (-2, 1), 
    (-1, -2), (-1, 2), 
    (1, -2), (1, 2), 
    (2, -1), (2, 1)
]

for move_x, move_y in moves:
    posib_move_x = x + move_x
    posib_move_y = y + move_y
    
    if 0 <= posib_move_x < 8 and 0 <= posib_move_y < 8:
        board[posib_move_x][posib_move_y] = '*'

for row in board:
    print(*row)