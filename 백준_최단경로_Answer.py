from sys import stdin
import sys
from collections import defaultdict
import heapq

V, E = list(map(int, stdin.readline().split()))
start = int(stdin.readline())
d = defaultdict(list)   # 연결 네트워크
dist = defaultdict(int) # 각 노드까지의 최소비용을 기록할 딕셔너리

for _ in range(E):
    u,v,w = list(map(int,stdin.readline().split()))
    d[u].append((w,v))


# 최단거리 기록 딕셔너리를 INF로 초기화
for i in range(1, V + 1):
    dist[i] = sys.maxsize
dist[start] = 0

def dijkstra(st):   # start지점 부터 시작해 최소비용 구하기

    q = []
    heapq.heappush(q,(0,st))
    while(q):

        cost, s = heapq.heappop(q)
        if dist[s] < cost:
            continue
        #sub = sorted(d[s], key = lambda x: x[1])
        for c, e in d[s]:
            if dist[e] > (cost+c):
                dist[e] = (cost+c)
                heapq.heappush(q,(cost+c,e))


dijkstra(start)

# print(dist)
for k,v in dist.items():
    if v == sys.maxsize:
        print("INF")
    else:
        print(v)