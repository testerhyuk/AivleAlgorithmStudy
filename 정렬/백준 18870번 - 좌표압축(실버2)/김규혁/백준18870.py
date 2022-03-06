n = int(input())

coordinate = list(map(int, input().split()))
idx = list(set(coordinate))
idx.sort()

dic = dict()

for i in range(len(idx)):
    dic[idx[i]] = i

for i in coordinate:
    print(dic[i], end=' ')