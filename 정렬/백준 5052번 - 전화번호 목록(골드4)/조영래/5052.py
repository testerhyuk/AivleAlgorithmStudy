import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    numbers.sort()
    for i in range(n - 1):
        if numbers[i] == numbers[i + 1][: len(numbers[i])]:
            print("NO")
            break
    else:
        print("YES")
