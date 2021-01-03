from sys import stdin
from collections import defaultdict

n=int(stdin.readline())
lst=[]
for _ in range(n):
    lst.append(list(stdin.readline())[:-1])

# print(n)
# print(lst)

count=1
d=defaultdict(int)

def dfs(i,j):
    if i<0 or i>=n or j<0 or j>=n or lst[i][j]!='1':
        return
    lst[i][j]='0'
    d[count]+=1
    dfs(i+1,j)   # 하
    dfs(i-1,j)   # 상
    dfs(i,j+1)   # 우
    dfs(i,j-1)   # 좌


for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j]=='0':
            continue
        else:
            dfs(i, j)
            count+=1


# 출력
print(len(d))
output=sorted(d.values())
for i in output:
    print(i)