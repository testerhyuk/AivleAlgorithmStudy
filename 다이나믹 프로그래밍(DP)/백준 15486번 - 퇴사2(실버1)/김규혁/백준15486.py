import sys

sys.stdin = open('input.txt')

n = int(input())

schedule = [(0, 0)]

for _ in range(n):
    t, b = map(int, input().split())
    schedule.append((t, b))

dp = [0] * (n + 2)

for day in range(n, 0, -1):
    duration, wage = schedule[day]
    next_day = day + duration

    if next_day > n + 1:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], dp[next_day] + wage)
print(dp[1])