import sys

sys.stdin = open("input.txt", "r")

t = int(input())


def check(phone, n):
    for i in range(n - 1):
        if phone[i] == phone[i + 1][0 : len(phone[i])]:
            return "NO"
    return "YES"


# 틀린 코드
# def check(phone, n):
#     for i in range(n-1):
#         if phone[i] in phone[i+1]: -> 이 부분이 왜 안되는지 모르겠음
#             return 'NO'
#     return 'YES'

for _ in range(t):
    n = int(input())
    phone = sorted([input() for _ in range(n)])
    print(check(phone, n))
