import sys

sys.stdin = open('input.txt')

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

cases = [0] * (k + 1)
cases[0] = 1

for i in coin:
    for j in range(i, k+1):
        cases[j] += cases[j - i]
print(cases[k])