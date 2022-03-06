import heapq

n, k = map(int, input().split())

arr = list(map(int, input().split()))

cost_arr = []

for i in range(n - 1):
    heapq.heappush(cost_arr, arr[i + 1] - arr[i])

result = 0
for _ in range(n - k):
    result += heapq.heappop(cost_arr)

print(result)
