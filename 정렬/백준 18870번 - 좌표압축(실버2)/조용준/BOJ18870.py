# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# arr_sort = sorted(list(set(arr)))

# for coord in arr:
#     print(arr_sort.index(coord), end=' ')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr_sort = sorted(list(set(arr)))

dict = {arr_sort[i]: i for i in range(len(arr_sort))}

for coord in arr:
    print(dict[coord], end=' ')