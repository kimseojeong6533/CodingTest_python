from sys import stdin
from collections import defaultdict
N, M =list(map(int,stdin.readline().split()))  # 정점의 개수(N), 간선의 개수(M)

d=defaultdict(list)
for _ in range(M):
    a, b = list(map(int, stdin.readline().split()))
    d[a]+=[b]
    d[b]+=[a]

# print(d)

visit=[0]*(N+1)
answer=0

def dfs(num):
    if visit[num]!=0:
        return
    visit[num]=1

    for k in d[num]:
        dfs(k)

for i in range(1,N+1):
    if visit[i]!=0:
        continue
    dfs(i)
    answer+=1

print(answer)