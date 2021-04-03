from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def dfs(a,b,weights,heights,visit,lst):
    if a<0 or a>=heights or b<0 or b>=weights or visit[a][b] == 1 or lst[a][b] == 0:
        return

    visit[a][b] = 1

    dfs(a - 1, b - 1, weights, heights, visit, lst)
    dfs(a - 1, b, weights, heights, visit, lst)
    dfs(a - 1, b+1, weights, heights, visit, lst)

    dfs(a, b+1, weights, heights,visit,lst)
    dfs(a, b-1, weights, heights,visit,lst)

    dfs(a + 1, b-1, weights, heights, visit, lst)
    dfs(a + 1, b, weights, heights, visit, lst)
    dfs(a + 1, b+1, weights, heights, visit, lst)
    return

def count_island(lst):

    weight = len(lst[0])
    height = len(lst)
    d = defaultdict(int)
    d[1] = 0   # island

    visit = [[0]*weight for _ in range(height)]

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 1 and visit[i][j] == 0:
                d[1] += 1
                dfs(i, j, weight, height, visit,lst)

    return d

answer = []
while(1):
    w, h = list(map(int,stdin.readline().split()))

    if w==0 and h==0:
        break

    maps = []
    for _ in range(h):
        tmp = list(map(int,stdin.readline().split()))
        maps.append(tmp)
    res = count_island(maps)
    answer.append(res[1])

for i in answer:
    print(i)


