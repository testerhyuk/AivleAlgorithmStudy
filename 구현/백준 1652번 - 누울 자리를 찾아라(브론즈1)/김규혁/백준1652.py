import sys
sys.stdin = open("input.txt", 'r')

n = int(input())

room = [input() for i in range(n)]

print(room)