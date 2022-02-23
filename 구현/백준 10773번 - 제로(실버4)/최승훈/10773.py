#https://www.acmicpc.net/problem/10773

stack = []

n = int(input())

for _ in range(n):
    k = int(input())
    if(k != 0):
        stack.append(k)
    else:
        stack.pop()

print(0 if len(stack) == 0 else sum(stack))