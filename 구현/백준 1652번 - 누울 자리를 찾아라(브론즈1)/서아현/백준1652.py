import sys

n = int(input())
ml=[]
for i in range(n):
    ml.append(list(input()))

cnt = 0

def row():
    room = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if ml[i][j] == '.':
                cnt+=1

            else:
                if cnt >= 2:
                    room += 1

                cnt = 0

        if cnt >= 2:
            room += 1
    
def col():
    room = 0
    for j in range(n):
        cnt = 0
        for i in range(n):
            if ml[i][j] == '.':
                cnt+=1

            else:
                if cnt >= 2:
                    room += 1

                cnt = 0

        if cnt >= 2:
            room += 1
    

print(row(), col())