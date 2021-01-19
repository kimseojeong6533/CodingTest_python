from sys import stdin

N, K = list(map(int,stdin.readline().split()))

lst = list(map(int,stdin.readline().split()))

belt=[]
lst1=lst[:N]
lst2=lst[N:]
belt=[lst1,lst2[::-1]]

#print(belt)  # 안에 요소값 = 내구도
#print()

#          오른쪽   왼족  아래로  위로
direction=[(0,1),(0,-1),(1,0),(-1,0)]

robot=[]

cnt=1 # 단계

while(1):

    # 벨트 회전
    ru=belt[0][N-1]
    ld=belt[1][0]
    tmp0=belt[0][0:N-1]
    tmp1=belt[1][1:N]
    belt=[[ld]+tmp0,tmp1+[ru]]

    #print('벨트 회전후 : ',belt)

    # 벨트회전에 따라 로봇도 회전
    n_robot=[]
    d=0
    while robot:
        i,j = robot.pop(0)
        if i==0:
            if j==N-1:
                d=2
                #continue
            else:
                d = 0
        else:
            if j==0:
                d = 3
            else:
                d = 1

        x, y = i+direction[d][0], j+direction[d][1]
        if x==0 and y==N-1:
             continue
        n_robot.append((x,y))

    robot=[x for x in n_robot]
    #print('컨베이어벨트 회전후, 로봇위치 : ',robot)

    # 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동
    new_robot=[]
    d=0
    while robot:
        (i, j) = robot.pop(0)      # 벨트에 올라간 로봇순서대로
        if i==0:
            if j==N-1:  # 내려가는 위치이면
                d=2
                continue
            else:  # 방향은 오른쪽
                d=0

        else:
            if j==0:   # 방향은 위로  # 올라가는 위치
                d=3

            else:  # 방향은 왼쪽
                d=1

        # 이동할 칸 = x, y
        x = i + direction[d][0]
        y = j + direction[d][1]


        if belt[x][y] >= 1 and (x,y) not in new_robot and (x,y) not in robot:  # 내구도가 1이상이고 이동할 칸에 로봇이 없다면
            if x==0 and y==N-1:
                belt[x][y] -= 1
                continue
            else:
                new_robot.append((x, y))
                belt[x][y] -= 1  # 로봇이 올라가면 내구도 = 내구도-1
        else:
            new_robot.append((i,j))  # 조건을 만족하지않으면 가만히

    robot=[x for x in new_robot]
    #print('로봇 이동 후 : ', robot)


    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if belt[0][0]>0:
        robot.append((0,0))
        belt[0][0]-=1  # 로봇이 칸에 올라가면 즉시 내구도가 1만큼 감소

    #print('올라가는 위치 고려후 robot : ', robot)
    #print('올라가는 위치 고려후  belt : ',belt)

    # 내구도가 0인 칸의 개수가 K개 이상이라면 break, 아니면 continue
    kan=0
    for i in range(2):
        for j in range(N):
            if belt[i][j] == 0:
                kan+=1

    #print('단계 : ', cnt)
    #print()

    if kan>=K:
        break

    cnt+=1




print(cnt)