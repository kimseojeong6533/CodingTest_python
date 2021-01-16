from sys import stdin
from itertools import combinations
N, M = list(map(int, stdin.readline().split()))  # 세로, 가로


direction=[(1,0),(-1,0),(0,1),(0,-1)]
lst=[]
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))


virus=[]
binkan=[]
wall=[]
for i in range(N):
    for j in range(M):
        if lst[i][j]==2:
            virus.append((i,j))
        elif lst[i][j]==0:
            binkan.append((i,j))
        else:
            wall.append((i,j))


# 빈칸인 곳을 잠재적인 벽이라고 생각한다
wall_maria=list(map(list,combinations(binkan, 3)))
safezone=0  # 안전영역의 최댓값을 구하라

while wall_maria:
    #walls=

    new_wall = wall[:] + wall_maria.pop(0)   # 기존 벽 + 새로운 3개의 벽

    lst2=[[0]*M for _ in range(N)]

    for x,y in new_wall:
        lst2[x][y]=1

    for x, y in virus:
        lst2[x][y]=2

    # 바이러스가 퍼짐
    active_virus = virus[:]
    while active_virus:
        x,y = active_virus.pop(0)
        for d in direction:
            new_x=x+d[0]
            new_y=y+d[1]

            if new_x<0 or new_x>=N or new_y<0 or new_y>=M or lst2[new_x][new_y]!=0:
                continue

            lst2[new_x][new_y]=2
            active_virus.append((new_x,new_y))

    cnt=0
    for i in range(N):
        for j in range(M):
            if lst2[i][j]==0:
                cnt+=1

    safezone=max(safezone,cnt)

print(safezone)



