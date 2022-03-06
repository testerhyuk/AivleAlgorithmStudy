#https://www.acmicpc.net/problem/5052

import sys
import copy

t = int(sys.stdin.readline())

results = []

for _ in range(t):
    n = int(sys.stdin.readline())
    phones = []
    for _ in range(n):
        phones.append(str(sys.stdin.readline().rstrip()))
    
    phones.sort(key = lambda x : len(x))

    count = 0
    groups = [phones]
    is_const = True
    MAX_COUNT = len(phones[n-1])

    while(True):
        New_groups =[]
        for group in groups:
            if(len(group) <2):
                continue
            else:
                stack = []
                for phone in group:
                    if(len(phone) == count):
                        is_const = False
                        break

                    ch = phone[count]
                    try:
                        idx = stack.index(ch)
                    except:
                        idx = -1
                    if(idx == -1):
                        stack.append(ch)
                        New_groups.append([phone])
                    else:
                        if(len(phone)-1 == count):
                            is_const = False
                        New_groups[idx].append(phone)

        if(not is_const):
            break
        groups = copy.deepcopy(New_groups)
        count += 1
        
        if(MAX_COUNT == count):
            break    


            
    results.append("YES" if is_const else "NO")

print("\n".join(results))