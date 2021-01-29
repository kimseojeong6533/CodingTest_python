from sys import stdin
from collections import defaultdict
import copy
#              0        1       2       3       4      5      6       7
direction = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

lst=[]
for _ in range(4):
    lst.append(list(map(int, stdin.readline().split())))

# print(lst)

fish = defaultdict(list)
lst2 = []

for i in range(4):
    sub=[]
    for j, k  in zip(range(0, len(lst[i]), 2), range(4)):
        sub.append(lst[i][j])    # 지도
        fish[lst[i][j]] += [lst[i][j+1]-1, i, k]  # [방향, x, y]
    lst2.append(sub)



# 상어가 처음에 (0,0)을 차지 -> 해당 자리에 있던 물고기의 방향을 가지게 됨.

#sx, sy = 0, 0  # 현재 상어의 위치
#sd = fish[lst2[0][0]][0] # 현재 상어의 방향

#ans = 0  # 상어가 먹은 물고기 번호
#ans += fish[lst2[0][0]]
#fish[lst2[0][0]] = [-1, 0, 0]   # fish사전에서 해당 물고기번호key를 지움
#lst2[0][0]=0


# print('초기 fish : ', fish)
# print('초기 lst2 : ',lst2)
# print()

#while(1):

def dfs(sx, sy, ans, sd, lst2, fish):
    global answer
    # print('상어의 위치 : ', sx, sy, ' | 방향 : ',sd, 'ans : ',ans)
    # print('물고기 자리 : ', lst2)

    # for k, v in fish.items():
    #     if v[0]== -1:
    #         print('k : ',k,'v : ',v)
    fish[lst2[sx][sy]] = [-1, sx, sy]  # fish사전에서 해당 물고기번호key를 지움

    #물고기가 번호순으로 이동한다
    f = sorted(list(fish.keys()))
    for i in f:
        if fish[i][0] == -1:
            continue

        d, x, y = fish[i][0], fish[i][1], fish[i][2]
        new_d = d

        while(1):

            nx = x + direction[new_d][0]
            ny = y + direction[new_d][1]
            #print(i, new_d, x, y, nx, ny, d)
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == sx and ny == sy):  # 상어가 있거나 격자에서 벗어날 경우, 이동 불가
                new_d += 1
                if new_d > 7:
                    new_d = 0
                if new_d == d:
                    break
                continue

            # 물고기끼리 자리 바꿈
            nn = lst2[nx][ny]
            nd = fish[nn][0]

            fish[i] = [new_d, nx, ny]
            fish[nn] = [nd, x, y]

            #print(x, y,' : ',i,new_d,' | ',nx, ny,' : ',nn, nd)
            lst2[nx][ny] = i
            lst2[x][y] = nn
            break

    # print('final lst2 : ', lst2)


    # 상어가 이동
    cnt=1

    while(cnt <= 4):
        cnt += 1
        sx = sx + direction[sd][0]
        sy = sy + direction[sd][1]
        if 0 <= sx < 4 and 0 <= sy < 4 and fish[lst2[sx][sy]][0] != -1: # 격자에 있고, 빈칸이 아닌 곳이라면
            #print(sx, sy)
            lst3 = copy.deepcopy(lst2)
            fishs = copy.deepcopy(fish)
            # print('전 - answer : ', answer, ' ans : ', ans, ' / ', lst3[sx][sy])

            answer = max(answer, ans + lst3[sx][sy])
            # print('후 - answer : ', answer, ' ans : ', ans, ' / ', lst3[sx][sy])
            # print()
            dfs(sx,sy,ans+lst2[sx][sy], fishs[lst2[sx][sy]][0], lst3, fishs)  # 상어의 x, 상어의 y, 상어가 먹은 물고기번호, 먹은 물고기 번호, 해당 물고기의 방향

            #print('ans : ', ans+lst3[sx][sy], 'answer : ', answer)
        else:
            # print('NO---')
            continue


answer = lst2[0][0]
dfs(0, 0, lst2[0][0], fish[lst2[0][0]][0], lst2, fish)
print(answer)
