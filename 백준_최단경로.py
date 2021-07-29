## 시간초과

from sys import stdin
import sys
from collections import defaultdict

V, E = list(map(int, stdin.readline().split()))
start = int(stdin.readline())
d = defaultdict(list)

for _ in range(E):
    u,v,w = list(map(int,stdin.readline().split()))
    d[u].append((v,w))


def FindShortestDistance(e):
    # s -> e까지의 최단거리 구하기
    q = [(1,0)]
    ans = sys.maxsize
    visit = [0]*V

    while(q):
        st,c = q.pop(0)
        visit[st-1]=-1
        for next_n, weight in d[st]:
            if visit[next_n-1]!=-1:
                if next_n == e and ans > (c+weight):
                    ans = c+weight
                else:
                    q.append((next_n,c+weight))
    return ans



res = defaultdict(int)
for i in range(start,V+1):
    if i == start:
        res[i]=0
    else:
        res[i]=FindShortestDistance(i)
for k,v in res.items():
    if v == sys.maxsize:
        print("INF")
    else:
        print(v)








