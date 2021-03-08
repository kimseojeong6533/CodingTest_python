# 다익스트라(그래프내 한정점에서 다른 정점까지의 최소 길이 구하기)
from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
N,M,X = list(map(int,stdin.readline().split()))

d=defaultdict(list)
for _ in range(M):
    s,e,c = list(map(int,stdin.readline().split()))
    d[s]+=[(c,e)]

# 학생들이 집에서 X에 갈때의 최단비용거리 계산
res = {k:v for k,v in zip(range(1,N+1),[0]*(N+1))}
def go(a,cost,visit,init):

    if a == X:
        if res[init]==0:
            res[init]=cost
        else:
            res[init] = min(res[init],cost) # res : 각 마을에서부터 X에 도착하는데 가장 비용이 적은 값이 들어가는 사전

        return
    for c,n in d[a]:
        if visit[n]==0:
            visit2 = [x for x in visit]  # 방문 마을을 확인하기위한 visit
            visit2[n]=1
            go(n,cost+c,visit2,init)
    return

for i in range(1,N+1):
    visits=[0]*(N+1)
    visits[i]=1
    go(i,0,visits,i)

# 학생들이 X에서 집에 올 때의 최단비용거리 계산
res2 = {k:v for k,v in zip(range(1,N+1),[0]*(N+1))}
def come(start,cost,visit,init):

    if start==init:
        if res2[init]==0:
            res2[init]=cost  # res2 : X에서 각 마을노드까지의 최단비용거리가 값으로 들어감
        else:
            res2[init] = min(res2[init],cost)
        return

    for c,n in d[start]:
        if visit[n]==0:
            visit2 = [x for x in visit]
            visit2[n]=1
            come(n,cost+c,visit2,init)
    return

for i in range(1,N+1):
    visits = [0]*(N+1)
    visits[X]=1
    come(X,0,visits,i)  # X:출발, i : 도착

# 오고갈때의 비용값을 합해서, 가장 클때의 key값을 출력
tmp = {k:v for k,v in zip(range(1,N+1),[0]*(N+1))}
x=1
for i,j in zip(list(res.values()),list(res2.values())):
    tmp[x]=(i+j)
    x+=1
print(sorted(tmp.items(),key=lambda x: -x[1])[0][1])

