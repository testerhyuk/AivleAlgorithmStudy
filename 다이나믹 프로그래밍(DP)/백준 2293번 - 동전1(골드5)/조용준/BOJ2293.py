import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
dp[1] = 1

coins = [int(input()) for _ in range(n)]

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] = dp[i] + dp[i - coin]

print(dp[k])
