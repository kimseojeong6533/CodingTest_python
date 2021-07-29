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
    visit[num]=1

    for i in range(1, V + 1):
        dist[i] = sys.maxsize
    dist[num] = 0


    for e, c in d[num]:  # 현재 연결된 노드상태에 따른 거리를 기록함
        if dist[e] > c:
            dist[e] = c


    while(q):

        node = q.pop(0)
        print('node : ',node)
        val = node
        min_val = sys.maxsize

        for e, c in d[node]:    # 현재 노드에 연결된 노드중, 가장 최소비용을 가진 노드를 선택하는 과정
            if visit[e]==0:
                print('e : ',e)
                q.append(e)
                if min_val > c:
                    min_val = c
                    val = e

        visit[val] = 1   # val : 현재 노드에 연결되어 있으면서 가장 최소비용을 가진 노드번호 -> 방문 처리
        print('val : ',val)
        print('visit : ',visit)
        for e,c in d[val]:
            if dist[e] > dist[val] + c:
                dist[e] = dist[val] + c
        print('dist : ',dist)
        print()
    for i in dist.values():
        if i == sys.maxsize:
            print("INF")
        else:
            print(i)
    return


dijkstra(start)
