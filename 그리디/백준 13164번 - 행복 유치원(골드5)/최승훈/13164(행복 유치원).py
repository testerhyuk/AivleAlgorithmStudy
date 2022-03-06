#https://www.acmicpc.net/problem/13164
import sys

N, K = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

dist = []

for i in range(1, N):
    dist.append(height[i] - height[i-1])

dist.sort()

print(sum(dist[:N-K]))
