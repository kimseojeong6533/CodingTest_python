from sys import stdin
from collections import defaultdict
import sys
N,M,X = list(map(int,stdin.readline().split()))

course = [[sys.maxsize]*(N) for _ in range(N)]

for _ in range(M):
    start,end,cost = list(map(int,stdin.readline().split()))
    course[start-1][end-1] = cost

# 각 노드의 최단거리를 INF로 초기화
go = defaultdict(int)
for i in range(1,N+1):
    go[i] = sys.maxsize
go[X]=0

# 시작노드에 연결된 지점을 반영
for i in range(len(course[X])):
    if course[X-1][i] < sys.maxsize:
        go[i+1] = course[X-1][i]

visit = [0]*(N+1)

print(course)
print(go)

#각 노드에서 X노드에까지 최단거리를 구함

v=-1
q=[X]
while(q):
    node = q.pop(0)

    min_val = sys.maxsize
    for j in range(1,len(course[node-1])+1):
        if visit[j] == 0 and min_val > go[j]:
            min_val = go[j]
            v = j
    visit[v] = 1  # 방문처리

    for j in range(1,N+1):
        if go[j] > go[v] + course[v-1][j-1]:
            go[j] = go[v] + course[v-1][j-1]

    print('v : ',v)
    break

print()
print(go)





