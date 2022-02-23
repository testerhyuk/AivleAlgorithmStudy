import sys


cnt = 0
n = int(input())
arr=[]
for i in range(n):
    i -= cnt
    arr.append(int(input()))
    if arr[i] == 0:
        del arr[i]
        i -= 1
        cnt+=1
        for i in range(len(arr)):
            if arr[i] != 0:
                del arr[i]
                cnt+=1
                break
                
            else :
                i-=1
                cnt+=1
                continue

print(arr)
                 
print(sum(arr))


# import sys

# sum = 0
# n = int(input())
# arr=[]
# arr = [0] * n

# for i in range(n):
#     arr[i] = int(input())

#     if arr[i] == 0:
#         i -= 1
#         while True:
#             if arr[i] == 0:
#                 i-=1
#                 continue
#             else :
#                 arr[i] = 0
#                 break
    
# for i in range(n):
#     sum += arr[i]

# print(sum)
