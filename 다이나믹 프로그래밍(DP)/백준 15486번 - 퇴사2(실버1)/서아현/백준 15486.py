import sys

N = int(sys.stdin.readline())

day = N
T, P = [0], [0]
dp = [0]*(N+2)

# 직관적으로 이해하기 쉽게 T,P[1]부터 저장
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])

# 마지막 날부터 거꾸로 진행
for i in range(N, 0, -1):
    # 상담은 당일부터 시작하므로 날짜+기간-1
    # 이 값이 퇴사일보다 작거나 같을 때
    if i + T[i] - 1 < N + 1:
        # i+1일 누적 급여 vs i일 급여 + 다음 상담 누적급여
        # P[i]+dp[i+T[i]]일 때 상담을 한 것
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

    else:    
        dp[i] = dp[i+1]

print(dp[1])
