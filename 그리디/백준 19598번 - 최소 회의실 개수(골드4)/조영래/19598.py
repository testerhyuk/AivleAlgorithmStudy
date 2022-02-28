import sys
input = sys.stdin.readline
import heapq

n = int(input())

List = []
for _ in range(n):
  start, end = map(int,input().split())
  List.append([start, end])

List.sort(key=lambda x:x[0])


result = [List[0][1]]
for i in range(1, n):
  if result[0] > List[i][0]: # heap이기때문에 result[0]은 최솟값이다.
    heapq.heappush(result, List[i][1])
  else:
    heapq.heappop(result)
    heapq.heappush(result, List[i][1]) # 최소값이 변경될 수 있다.

print(len(result))

# result = [List[0]]
# for i in range(1, len(List)):
#   for j in range(len(result)):
#     if List[i][0] >= result[j][1]:
#       result[j][1] = List[i][1]
#       break
#   else:
#     result.append(List[i])

# print(len(result))