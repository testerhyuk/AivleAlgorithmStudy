#https://www.acmicpc.net/problem/15486
#입력
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

import sys

N = int(sys.stdin.readline().rstrip())
Dp_arr = []

T = []
P = []

Dp_arr = [0] * (N+1)

for _ in range(N):
    Ti, Pi = map(int, sys.stdin.readline().split())
    T.append(Ti)
    P.append(Pi)

for i in range(0, N):
    if T[i] <= N - i:
        Dp_arr[i+T[i]] = max(Dp_arr[i+T[i]], Dp_arr[i]+P[i])
        
    Dp_arr[i+1] = max(Dp_arr[i+1], Dp_arr[i])

print(Dp_arr[N])

# for _ in range(N):
#     Ti, Pi = map(int, sys.stdin.readline().split())
#     T.append(Ti)
#     P.append(Pi)
#     Dp_arr.append({"end_day" : [], "sum" : []})

# #0일차
# Dp_arr[0]["end_day"].append(T[0])
# Dp_arr[0]["sum"].append(P[0])

# if(T[0] != 1):
#     Dp_arr[0]["end_day"].append(1)
#     Dp_arr[0]["sum"].append(0)

# for i in range(1,N):
#     for j in range(len(Dp_arr[i-1]["end_day"])):
#         if(T[i] + i <= N and Dp_arr[i-1]["end_day"][j] < i+1):
#             try:
#                 idx = Dp_arr[i]["end_day"].index(i+T[i])
#             except ValueError:
#                 idx = -1

#             if(idx == -1 or Dp_arr[i]["sum"][idx] < Dp_arr[i-1]["sum"][j] + P[i]):
#                 Dp_arr[i]["end_day"].append(i + T[i])
#                 Dp_arr[i]["sum"].append(Dp_arr[i-1]["sum"][j] + P[i])
#                 if(T[i] != 1):
#                     Dp_arr[i]["end_day"].append(Dp_arr[i-1]["end_day"][j])
#                     Dp_arr[i]["sum"].append(Dp_arr[i-1]["sum"][j])

#         else:
#             Dp_arr[i]["end_day"].append(Dp_arr[i-1]["end_day"][j])
#             Dp_arr[i]["sum"].append(Dp_arr[i-1]["sum"][j])


# print(max(Dp_arr[-1]["sum"]))