# from collections import defaultdict
n = int(input())

arr = list(map(int, input().split()))

arr_new = list(set(arr))
arr_new.sort()

Dict = {}

for i, v in enumerate(arr_new):
    Dict[v] = i

for ele in arr:
    print(Dict[ele], end=" ")

# n = int(input())

# arr = list(map(int, input().split()))

# arr_new = list(set(arr))
# arr_new.sort()

# Dict = {arr_new[i] : i for i in range(len(arr_new))}


# for ele in arr:
#     print(Dict[ele], end=" ")
