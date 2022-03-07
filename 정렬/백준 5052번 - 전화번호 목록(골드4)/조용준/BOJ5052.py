# 아직 맞았습니다! 를 못 받은 상태입니다. 밤에 고쳐볼게요..
import sys
input = sys.stdin.readline

t = int(input())

def check(num_list):
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1][0:len(num_list[i])]:
            print('NO')
    print('YES')

for _ in range(t):
    num_list = []
    n = int(input())
    for i in range(n):
        num_list.append(input().strip())
    num_list.sort()
    check(num_list)