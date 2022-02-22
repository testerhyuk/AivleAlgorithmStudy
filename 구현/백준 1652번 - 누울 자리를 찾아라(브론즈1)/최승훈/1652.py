#https://www.acmicpc.net/problem/1652

n = int(input())
arr = [list(input()) for _ in range(n)]

r_x = 0
r_y = 0

length = 0

#세로 구하기
for x in range(n):
    length = 0
    for y in range(n):
        if(arr[y][x] =='.'):
            length+=1
        else:
            if(length >=2):
                r_y +=1
            length = 0
    if(length >=2):
        r_y+=1

#가로 구하기
for y in range(n):
    length = 0
    for x in range(n):
        if(arr[y][x] =='.'):
            length+=1
        else:
            if(length >=2):
                r_x +=1
            length = 0
    if(length >=2):
        r_x+=1

print(r_x, r_y)