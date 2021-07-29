from sys import stdin
from collections import defaultdict
import sys
N,M,X = list(map(int,stdin.readline().split()))

course = defaultdict(list)
dist = defaultdict(int)  # start점에서 각자의 마을까지의 최단거리

for _ in range(M):
    start,end,cost = list(map(int,stdin.readline().split()))
    course[start] += [(end,cost)]


def dijkstra(num):
    q = [num]
    visit = [0] * (N + 1)
    visit[num] = 1

    for i in range(1, N + 1):
        dist[i] = sys.maxsize
    dist[num] = 0

    tmp = sys.maxsize
    for e, c in course[num]:
        if tmp > c:
            dist[e] = c
            tmp = c

    while(q):

        min_val = sys.maxsize
        node = q.pop(0)
        v = -1
        # for k,v in dist.items():  # 방문하지 않은 노드 중에서 가장 비용이 적은 노드 찾기
        #     if visit[k] == 0
        for e,c in course[node]:
            print(course)
            if visit[e] == 0:
                q.append(e)
                if min_val > c:
                    min_val = c
                    v = e

        visit[v] = 1


        for e,c in course[v]:
            if dist[e] > dist[v] + c:
                dist[e] = dist[v] + c
    return dist

come = []
go = {x:0 for x in range(1,N+1)}

for i in range(1,N+1):
    red = dijkstra(i)
    if i == X:
        come += list(red.values())
    else:
        go[i] = red[X]

# print()
# print('go : ',go)
# print('come : ',come)
res = [x+y for x,y in zip(list(go.values()),come)]
print(max(res))


'''
4 9 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
2 1 100
'''
