# https://www.acmicpc.net/board/view/34516 참고

from sys import stdin
import sys
from collections import defaultdict

V, E = list(map(int, stdin.readline().split()))
start = int(stdin.readline())
d = defaultdict(list)
dist = defaultdict(int)  # start에서 각 노드까지의 최단거리를 기록할 딕셔너리
for _ in range(E):
    u,v,w = list(map(int,stdin.readline().split()))
    d[u].append((v,w))


print('d : ',d)
def dijkstra(num):  # num에서 다른 모든 노드로 가는 최단경로 구하기
    q=[num]
    visit = [0]*(V+1)

    for i in range(1, V + 1):
        dist[i] = sys.maxsize
    dist[num] = 0


    for e, c in d[num]:  # 현재 연결된 노드상태에 따른 거리를 기록함
        if dist[e] > c:
            dist[e] = c


    while(q):

        node = q.pop(0)
        if visit[node] == 1:
            continue

        visit[node] = 1
        val = node
        min_val = sys.maxsize

        for e, c in d[node]:    # 현재 노드에 연결된 노드중, 가장 최소비용을 가진 노드를 선택하는 과정
            if min_val > dist[node] + c:
                min_val = dist[node] + c
                val = e

            if dist[e] > dist[node] + c:
                dist[e] = dist[node] + c

        q.append(val)

    for i in dist.values():
        if i == sys.maxsize:
            print("INF")
        else:
            print(i)
    return


dijkstra(start)
