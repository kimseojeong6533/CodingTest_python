from sys import stdin

direction = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

lst=[]
for _ in range(4):
    lst.append(list(map(int, stdin.readline().split())))

fish = []
for i in range(4):
    sub=[]
    for j in range(0, len(lst[i]), 2):
        sub.append([i, j, lst[i][j], lst[i][j+1]-1])
    fish.append(sub)

#print(fish)

# 0,0자리에 상어가 자리잡음,
shark = [0, 0, fish[0][0][2], fish[0][0][3]]
#shark_sum = fish[0][0][2]
fish[0][0]=0
#sx, sy = 0, 0  # 상어의 위치

ans = 0


print('초기 fish : ', fish)
# 상어가 이동

def dfs(sx, sy, sharkn, sharkd, fish):
    print('상어의 위치 : ', sx, sy,'공간 : ',fish)
    print()
    global ans
    fish[sx][sy] = 0
    fish.sort(key = lambda x : x[2])
    # 물고기가 이동 (1번 물고기부터 n번 물고기 까지 차례대로 이루어짐)
    for fi in fish:
        for f in fi:
            if f == 0:
                continue
            x, y, n, d = f
            print(x,y,n,d)
            new_d = d

            while (1):

                nx = x + direction[new_d][0]
                ny = y + direction[new_d][1]


                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    new_d += 1
                    if new_d > 7:
                        new_d = 0

                    if new_d == d:
                        break
                    continue

                if (fish[nx][ny] == 0) or (nx == sx and ny == sy):  # 해당 칸에 물고기가 없거나, 상어가 있으면
                    new_d += 1
                    if new_d > 7:
                        new_d = 0

                    if new_d == d:
                        break
                    continue

                shiftx, shifty, shiftn, shiftd = fish[nx][ny]  # 원래 해당칸에 있는 물고기 정보

                fish[x][y], fish[nx][ny] = [x, y, shiftn, shiftd], [nx, ny, n, d]  # 물고기들끼리 자리를 바꿈
                print('i,j - nx, ny',fish[x][y], fish[nx][ny])
                break

    print('fish : ', fish)
    # 상어가 이동
    nx, ny = sx, sy

    while(1):

        nx = nx + direction[sharkd][0]
        ny = ny + direction[sharkd][1]
        print('nx : ', nx, 'ny : ',ny)
        print('fish[nx][ny] : ', fish[nx][ny])
        if nx < 0 or nx >= 4 or ny < 0 or ny <= 4:
            break


        if fish[nx][ny] == 0:
            continue

        print(9999)
        sharkd = fish[nx][ny][3]
        sx, sy = nx, ny
        print(fish[nx][ny])
        #nshark = [sx, sy, sh[2]+fish[nx][ny][2], sharkd]
        dfs(sx, sy, sharkn+fish[nx][ny][2], sharkd, fish)


    ans = max(ans, sharkn)

dfs(0, 0, shark[2], shark[3], fish)

print(ans)