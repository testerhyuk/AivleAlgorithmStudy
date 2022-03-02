import sys
import heapq

num = int(sys.stdin.readline())
room=[]
for i in range(num):
    room.append(list(map(int, sys.stdin.readline().split())))

#회의 시작시간이 작은 순서대로 정렬
room.sort()

room_end = [0]


for start, end in room:

    #저장된 종료시간들의 최소값보다 현재 시작시간이 작으면 
    #새로운 heap 생성
    if room_end[0] > start:
        heapq.heappush(room_end, end)


    #현재 시작시간이 저장되어있는 저장된 종료시간보다 클 경우
    #방의 종료시간이 최솟값인 heap을 현재 종료시간으로 저장
    else:
        heapq.heappushpop(room_end, end)
        
        

print(len(room_end))
