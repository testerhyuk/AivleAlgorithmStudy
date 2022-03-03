# 참고: https://pacific-ocean.tistory.com/270

from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')

t = int(input())
dir = [(-1, 0), (1, 0), (0, -1), (0,1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                field[nx][ny] = 0
                q.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    for nx in range(n):
        for ny in range(m):
            if field[nx][ny] == 1:
                bfs(nx, ny)
                field[nx][ny] = 0
                cnt += 1
    print(cnt)