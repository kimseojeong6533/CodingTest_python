from sys import stdin
from itertools import combinations
import sys

direction=[(1,0),(-1,0),(0,1),(0,-1)]

N, M =list(map(int, stdin.readline().split()))

lst=[]
for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))

virus=[(i,j)for i in range(N) for j in range(N) if lst[i][j]==2]  # 활성 + 비활성

# 활성 바이러스의 경우의 수를 계산

vir=list(map(list,combinations(virus,M)))
answer=sys.maxsize
len_vir=len(vir)


while vir:
    active_vir = vir.pop(0)

    lst2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:  # 벽
                lst2[i][j] = -1
            elif lst[i][j] == 2:  # 바이러스인데
                if (i, j) in active_vir:  # 활성 바이러스이면
                    lst2[i][j] = 0  # -1 -> 0
                else:  # 비활성 바이러스이면
                    lst2[i][j] = -2

    poza=active_vir[:]

    while poza:
        lst3=[lst2[i] for i in range(N)]

        x,y=poza.pop(0)
        for d in direction:
            new_x=x+d[0]
            new_y=y+d[1]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or lst2[new_x][new_y] == -1:  # 인덱스를 넘거나 벽을 만나면
                continue

            if lst2[new_x][new_y] == 0 and (new_x, new_y) not in active_vir:  # 그냥 빈칸 일때,
                lst2[new_x][new_y] = lst2[x][y] + 1
                poza.append((new_x, new_y))

            elif lst2[new_x][new_y] == -2:  # 비활성 바이러스를 만났을 때,
                lst2[new_x][new_y] = lst2[x][y]+1
                poza.append((new_x, new_y))
                active_vir.append((new_x,new_y))

    cnt=0
    max_val=0
    for i in range(N):
        for j in range(N):
            if lst2[i][j]==0 and (i,j) not in active_vir:  # 진짜 빈칸만 찾는다
                cnt+=1
            if lst2[i][j]!=-1 and (i,j) not in active_vir:  # 벽이 아니면서 활성 바이러스 자리도 아닐때
                max_val=max(max_val,lst2[i][j])


    if cnt==0:
        answer = min(answer, max_val)

if answer==sys.maxsize:
    print(-1)
else:
    print(answer)