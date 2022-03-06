#https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline().rstrip())

datas = []
answer = [0] * N
compression = []

X = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    datas.append({
        "idx" : i,
        "key" : X[i]
    })
datas.sort(key = lambda x : x["key"])


answer[datas[0]["idx"]] = 0
count = 0

for i in range(1,N):
    if(datas[i-1]["key"] == datas[i]["key"]):
        answer[datas[i]["idx"]] = answer[datas[i-1]["idx"]]
    else:
        answer[datas[i]["idx"]] = answer[datas[i-1]["idx"]] + 1


for a in answer:
    print(a, end = " ")