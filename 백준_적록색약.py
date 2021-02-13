from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
N = int(stdin.readline())

lst = []
for _ in range(N):
    lst.append(list(stdin.readline())[:N])

#print('lst : ',lst)
#print()

visit_normal = [[0]*(N) for _ in range(N)]
visit_color = [[0]*(N) for _ in range(N)]

normal_d = defaultdict(int)
blind_d = defaultdict(int)

def dfs_normal(x,y,m):
    if x < 0 or x >= N or y < 0 or y >= N or visit_normal[x][y] == 1 or lst[x][y] != m:
        return

    visit_normal[x][y] = 1
    dfs_normal(x+1, y, m)
    dfs_normal(x-1, y, m)
    dfs_normal(x, y+1, m)
    dfs_normal(x, y-1, m)


def dfs_color(x,y,m):
    if x < 0 or x >= N or y < 0 or y >= N or visit_color[x][y] == 1 or lst[x][y] not in m:
        return

    visit_color[x][y] = 1
    dfs_color(x + 1, y, m)
    dfs_color(x - 1, y, m)
    dfs_color(x, y + 1, m)
    dfs_color(x, y - 1, m)


for i in range(N):
    for j in range(N):
        if visit_normal[i][j] == 0:
            if lst[i][j] == 'B':
                normal_d['B'] += 1
                dfs_normal(i, j,'B')

            elif lst[i][j] == 'R':
                normal_d['R'] += 1
                dfs_normal(i, j,'R')

            else:
                normal_d['G'] += 1
                dfs_normal(i,j,'G')

for i in range(N):
    for j in range(N):
        if visit_color[i][j] == 0:
            if lst[i][j] == 'B':
                blind_d['B'] += 1
                dfs_color(i, j, 'B')

            else:
                blind_d['RG'] += 1
                dfs_color(i, j, 'RG')

#print(normal_d)
#print(blind_d)
print(sum(list(normal_d.values())),sum(list(blind_d.values())))

