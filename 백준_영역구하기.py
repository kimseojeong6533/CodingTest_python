from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

M, N, K = list(map(int, stdin.readline().split()))

lst = []
for _ in range(K):
    lst.append(list(map(int, stdin.readline().split())))

paper = [[0] * (N) for _ in range(M)]
# print(paper)

for i in lst:
    for x in range(i[1], i[3]):
        for y in range(i[0], i[2]):
            #print(x,y)
            paper[x][y] = 1

#print(paper)

count = 0
d = defaultdict(int)


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or paper[x][y] == 1:
        return

    d[count] += 1
    paper[x][y] = 1  # 방문처리대신
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


for i in range(M):
    for j in range(N):
        if paper[i][j] == 1:
            continue
        dfs(i, j)
        count += 1

# print(d)
answer = sorted(d.values())
print(len(answer))
for i in answer:
    print(i, end=' ')
