import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

room = [input() for i in range(n)]
row, col = 0, 0

for i in range(n):
    row_seat, col_seat = 0, 0
    for j in range(n):
        # 가로
        if room[i][j] == '.':
            row_seat += 1
        else:
            if row_seat >= 2:
                row += 1
            # 초기화
            row_seat = 0

        # 세로
        if room[j][i] == '.':
            col_seat += 1
        else:
            if col_seat >= 2:
                col += 1
            # 초기화
            col_seat = 0

    if row_seat >= 2:
        row += 1
    
    if col_seat >= 2:
        col += 1

print(row, col)