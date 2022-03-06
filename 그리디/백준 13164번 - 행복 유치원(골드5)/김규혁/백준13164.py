import sys

sys.stdin = open('input.txt', 'r')

# 스스로 못품..
n, k = map(int, input().split())
kd = sorted(list(map(int, input().split())))

cost = []

for i in range(n-1):
    cost.append(kd[i+1] - kd[i])

cost.sort()

print(sum(cost[:n-k]))