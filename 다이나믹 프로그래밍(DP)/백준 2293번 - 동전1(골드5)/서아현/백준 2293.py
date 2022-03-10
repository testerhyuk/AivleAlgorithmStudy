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
        # 동전의 최소 가치부터 실행
        if j - i >= 0:
            # 구하려는 값에서 현재 동전가치를 뺀 값의 경우의 수를 가져오면 된다
            # 동전:2 값:5 ---> 5-2=3 / 3을 만드는 경우에 '+2' 를 해주면 5이기 때문
             dp[j] += dp[j - i]
print(dp[info[1]])
