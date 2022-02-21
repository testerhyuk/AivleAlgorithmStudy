import sys

sys.stdin = open('input.txt', 'r')

k = int(input())
s = [0]

for _ in range(k):
    n = int(input())

    if n == 0:
        s.pop()
    else:
        s.append(n)
print(sum(s))