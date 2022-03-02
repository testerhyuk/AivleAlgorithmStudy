# # 시간 기준 검색

# n = int(input())

# data = []
# count = 0
# result = 0

# for _ in range(n):
#     inroom, outroom = map(int,input().split())
#     data.append((inroom, 1))
#     data.append((outroom, -1))

# data.sort(key=lambda x: (x[0],x[1]))

# for _, ud in data:
#     count+= ud
#     result = max(result,count)

# print(result)



#우선순위 큐 알고리즘

# import heapq

# n = int(input())
# data = []
# for _ in range(n):
#     data.append(list(map(int,input().split())))

# data.sort(key=lambda x: (x[0]))

# rooms = [0]
# answer = 1
# for inroom, outroom in data:
#     if inroom >= rooms[0]:
#         heapq.heappop(rooms)
#     else:
#         answer+=1
#     heapq.heappush(rooms,outroom)

# print(answer)


#우선순위 큐 

from collections import deque

def heappop(heap : deque):
    res = heap.popleft()

    if(len(heap) == 0):
        return res
 
    heap.appendleft(heap.pop())

    idx = 0

    while(idx *2 + 1 < len(heap)):
        next = idx
        left = idx *2 + 1
        right = idx * 2 + 2

        if(heap[left] < heap[next]):
            next = left
        
        if(right < len(heap) and heap[right] < heap[next]):
            next = right
        
        if(idx== next):
            break
        
        heap[idx], heap[next] = heap[next], heap[idx]
        idx = next
    
    return res

def heappush(heap: deque, elem):
    heap.append(elem)

    idx = len(heap) - 1

    while(idx > 0):
        parent = int((idx-1) /2)

        if(heap[idx] < heap[parent]):
            heap[parent], heap[idx] = heap[idx], heap[parent]
        else:
            break

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x: (x[0]))


rooms = deque([0])
answer = 1

for inroom, outroom in data:
    if inroom >= rooms[0]:
        heappop(rooms)
    else:
        answer+=1
    heappush(rooms,outroom)

print(answer)