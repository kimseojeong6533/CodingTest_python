from sys import stdin
import collections

N=int(stdin.readline())
lst=[]
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

shark_size = 2  # 입력받았을 때의 아기상어 위치와 크기

tmp =[(i,j) for i in range(N) for j in range(N) if lst[i][j] == 9]
a, b = tmp[0][0], tmp[0][1]   # 입력받았을 때, 상어의 위치

direction=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i, j, distance, dist, s_size):
    q=collections.deque([(i,j,dist)])
    visit=[[0]*N for _ in range(N)]
    visit[i][j]=1

    while q:

        x, y, d = q.popleft()

        for dirs in direction:
            new_x=x+dirs[0]
            new_y=y+dirs[1]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or visit[new_x][new_y]==1 or s_size < lst[new_x][new_y]:
                continue

            visit[new_x][new_y] = 1

            if lst[new_x][new_y]>0 and lst[new_x][new_y]<s_size :
                distance.add((new_x, new_y, d+1))
            else:
                q.append((new_x, new_y, d + 1))


eating_time=0  # 먹기까지의 거리의 합
eating_cnt=0   # 먹는 횟수

while(1):

    sub=set()
    for i in range(N):
        for j in range(N):
            if lst[i][j]<=shark_size and lst[i][j]>0 and lst[i][j]!=9:
                sub.add((i,j))

    if not sub:
        break

    # 먹을 수 있는 물고기 각각의 위치와 거리를 구함
    distance = set()
    bfs(a, b, distance, 0, shark_size)
    distance_list=sorted(list(distance), key= lambda x : (x[2], x[0], x[1]))  # 거리, 가장 위에 있는 물고기, 가장 왼족에 있는 물고기순으로 정렬

    if not distance_list:
        break

    next_i, next_j, eating_dist = distance_list[0]
    eating_time += eating_dist # 먹는 시간 += 가기까지의 거리(eating)

    lst[a][b]=0  # 현재위치의 값은 0으로
    a, b = next_i, next_j
    lst[a][b]=9  # 다음 위치의 값은 9로

    eating_cnt += 1
    if eating_cnt == shark_size:  # 자기크기만큼 먹을 때 크기+1
        shark_size += 1
        eating_cnt = 0


print(eating_time)