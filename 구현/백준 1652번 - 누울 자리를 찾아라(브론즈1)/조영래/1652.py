n = int(input())

arr = [list(input()) for _ in range(n)]
hor=0 
ver=0
for i in range(n):
  hor_cnt = 0
  for j in range(n):
    if arr[i][j]=='.':
      hor_cnt+=1
    else:
      if hor_cnt >=2:
        hor+=1

      hor_cnt=0
  if hor_cnt>=2:
    hor+=1

for j in range(n):
  ver_cnt = 0
  for i in range(n):    
    if arr[i][j]=='.':
      ver_cnt+=1
    else:
      if ver_cnt >=2:
        ver+=1
      ver_cnt=0
  if ver_cnt>=2:
    ver+=1
      
print(hor)
print(ver)