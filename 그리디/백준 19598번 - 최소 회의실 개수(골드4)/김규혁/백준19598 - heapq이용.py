import heapq

n = int(input())

meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[0]))
 
et = [meeting[0][1]]
cnt = 1

for s, e in meeting[1:]:
    if s >= et[0]:
        heapq.heappop(et)
    else:
        cnt+=1
    heapq.heappush(et, e)
 
print(cnt)