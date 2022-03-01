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
        et.pop(0)
    else:
        cnt+=1
    et.append(e)
    et.sort()
 
print(cnt)