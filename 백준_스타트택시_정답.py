from sys import stdin

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M, fuel = list(map(int, stdin.readline().split()))

lst2 = []
for _ in range(N):
    lst2.append(list(map(int, stdin.readline().split())))

lst = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        lst[i][j] = -lst2[i][j]    # 벽을 -1로 처리


# 현재 기사의 위치,(1이상 N이하)
x, y = list(map(int, stdin.readline().split()))
x = x - 1
y = y - 1

# 승객의 정보
tmp = []
for _ in range(M):
    tmp.append(list(map(int, stdin.readline().split())))


# 0 ~ N-1로 표현하기위해 -1을 해줌
passenger = []
for a, b, a_i, b_j in tmp:
    passenger.append((a - 1, b - 1, a_i - 1, b_j - 1))


len_passenger = len(passenger)
flag = True


def shortest(x, y, pas, k):
    # (x,y) -> (px, py) 최단거리 계산
    q = [(x, y)]

    visit = [[0] * N for _ in range(N)]
    visit[x][y] = 1

    comp_lst = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            comp_lst[i][j] = lst[i][j]

    #print('최단거리 계산 전 lst : ', comp_lst)
    while q:
        (i, j) = q.pop(0)

        for d in direction:
            new_i = i + d[0]
            new_j = j + d[1]

            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N or comp_lst[new_i][new_j] == -1 or visit[new_i][new_j] !=0:
                continue
            visit[new_i][new_j] = 1
            comp_lst[new_i][new_j] = comp_lst[i][j] + 1
            q.append((new_i, new_j))

    #print('최단거리 계산 후 comp_lst : ',comp_lst)
    if k == 1:  # 손님들과 현재 택시기사의 위치중 최단거리를 뽑아 리턴
        distance = []
        for i, j, new_i, new_j in pas:
            if (comp_lst[i][j] >=0 and visit[i][j]==1):
                distance.append([comp_lst[i][j], i, j, new_i, new_j])
        return distance

    else:  # 손님의 현재위치에서 목적지위치까지 최단거리를 뽑아 리턴
        d_x, d_y = pas
        if comp_lst[d_x][d_y] >= 0 and visit[d_x][d_y] == 1:
            return comp_lst[d_x][d_y]
        else:   # 목적지에 도달할 수 없을 때
            return -1

while(flag):
    if passenger:
        shortest_dist = shortest(x, y, passenger, 1)
        shortest_dist.sort(key=lambda k: (k[0], k[1], k[2]))  # 최단거리, 행, 열 순으로 정렬

        if shortest_dist:
            dist, next_x, next_y, dest_x, dest_y = shortest_dist[0]  # 최단거리, 최단거리인 손님의 위치, 해당 손님의 목적지 위치
            if fuel - dist < 0:  # 이동하다가 연료가 바닥나면 이동이 실패하고 그날의 업무가 끝난다 또는 벽때문에 현재 손님의 위치까지 갈 수 없는 경우,
                flag = False
                break

            fuel = fuel - dist

            dist2 = shortest(next_x, next_y, [dest_x, dest_y], 2)  # 최단거리인 손님의 현재위치, [목적지위치]에서 손님의
            if dist2 == -1:
                flag = False
                break

            if fuel - dist2 < 0:  # 승객을 목적지까지 이동시키지 못했을 때, 또는, 목적지까지 벽대문에 도달할 수 없을 때
                flag = False
                break

            # 승객을 목적지까지 이동시켰을 경우
            fuel = fuel - dist2 + dist2 * 2  # - 목적지까지 최단거리 + 목적지최단거리 * 2
            x, y = dest_x, dest_y

            new_passenger = []
            while passenger:
                i = passenger.pop()
                if i == (next_x, next_y, dest_x, dest_y):
                    continue
                new_passenger.append(i)
            passenger=[x for x in new_passenger]

            len_passenger -= 1

        else:
            flag=False
            break
    else:
        if len_passenger==0:
            break
        else:
            flag=False
            break

if flag and len_passenger==0:
    print(fuel)
else:
    print(-1)



