import sys

info = list(map(int, sys.stdin.readline().split()))

num = []
for i in range(info[0]):
    num.append(int(sys.stdin.readline()))
num.sort()

dp = [0 for i in range(info[1] + 1)]
dp[0] = 1
for i in num:
    for j in range(1, info[1] + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[info[1]])
