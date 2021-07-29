from sys import stdin
import sys
from collections import defaultdict
import heapq

V, E = list(map(int, stdin.readline().split()))
start = int(stdin.readline())
d = defaultdict(list)
dist = defaultdict(int)  # start에서 각 노드까지의 최단거리를 기록할 딕셔너리
for _ in range(E):
    u,v,w = list(map(int,stdin.readline().split()))
    d[u].append((v,w))

# q를 힙큐 -> 비용 오름차순으로 정렬되도록 해야됌.


def dijkstra(num):  # num에서 다른 모든 노드로 가는 최단경로 구하기
    q = [(0,num)]
    heapq.heapify(q)
    visit = [0]*(V+1)

    for i in range(1, V + 1):
        dist[i] = sys.maxsize
    dist[num] = 0


    # for e, c in d[num]:  # 현재 연결된 노드상태에 따른 거리를 기록함
    #     if dist[e] > c:
    #         dist[e] = c

    while(q):

        cost,node = heapq.heappop(q)
        if visit[node] == 1:
            continue

        visit[node] = 1

        for e, c in d[node]:
            heapq.heappush(q, (c, e))
            if dist[e] > dist[node] + c:
                dist[e] = dist[node] + c

    for i in dist.values():
        if i == sys.maxsize:
            print("INF")
        else:
            print(i)
    return

dijkstra(start)
