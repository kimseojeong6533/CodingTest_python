from sys import stdin
from collections import defaultdict
import sys
import heapq

N,M,X = list(map(int,stdin.readline().split()))

course = [[sys.maxsize]*(N) for _ in range(N)]
d = defaultdict(list)
for _ in range(M):
    start,end,cost = list(map(int,stdin.readline().split()))
    d[start] += [(cost,end)]

dist_go = defaultdict(int)
dist_come = defaultdict(int)
res = defaultdict(int)
res[X] = 0

for i in range(1, N + 1):
    dist_come[i] = sys.maxsize
dist_come[X] = 0

def go(start, end):
    # start -> end 까지의 최소비용 구하기
    dist_temp = defaultdict(int)
    for i in range(1, N + 1):
        dist_temp[i] = sys.maxsize

    q = []
    heapq.heappush(q,(0,start))


    while(q):
        c, e = heapq.heappop(q)
        if e == end and dist_temp[e] > c:
            dist_temp[e] = c

        for weight, next_node in d[e]:
            if dist_temp[next_node] > (weight+c):
                dist_temp[next_node] = weight + c
                heapq.heappush(q,(weight+c,next_node))
    # print("start : ",start," / end : ",end)
    # print(dist_temp)
    # print()
    return dist_temp[end]

def come(start):
    q = []
    heapq.heappush(q,(0,start))

    while(q):
        c, e = heapq.heappop(q)
        if dist_come[e] < c:
            continue
        for weight, next_node in d[e]:
            if dist_come[next_node] > weight+c:
                dist_come[next_node] = weight + c
                heapq.heappush(q,(weight+c,next_node))



# go (i번 학생의 X네 마을에 갈 때, 각 학생에게 소요되는 최단비용)
for i in range(1,N+1):
    if i == X:
        continue
    res[i] = go(i,X)

# come : X마을에서 각 학생들의 마을로 가기까지의 소요되는 최단비용 구하기
come(X)
for k,v in dist_come.items():
    res[k] += v
# print(dist_come)
# print("res : ",res)
print(max(list(res.values())))



