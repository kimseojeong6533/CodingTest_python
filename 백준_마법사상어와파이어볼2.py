from sys import stdin
from collections import defaultdict

N,M,K = list(map(int,stdin.readline().split()))

fireball=[]
for _ in range(M):
    fireball.append(list(map(int,stdin.readline().split()))) # 행, 열, 질량, 속력, 방향

lst=[[0]*N for _ in range(N)]

fires=defaultdict(list)
while fireball:
    i,j,m,s,d = fireball.pop()
    fires[(i-1,j-1)]=[[i-1,j-1,m,s,d]]
    lst[i-1][j-1]=[[i-1,j-1,m,s,d]]  # 초기파이어볼 표시


# # #         0      1     2     3     4      5      6      7
direction=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

cnt=1
while(cnt<=K):

    new_fireball=defaultdict(list)  # 이동후의 파이어볼을 담을 사전
    for key,value in fires.items():
        for v in value:
            i,j,m,s,d = v[0], v[1], v[2], v[3], v[4]
            lst[i][j]=0
            next_x, next_y = i, j  # 속력만큼 이동하기위해, 초기화선언을 해줌
            mov = 0
            while (mov < s):  # 자신의 방향과 속력만큼 이동
                next_x = next_x + direction[d][0]
                next_y = next_y + direction[d][1]
                mov += 1

            next_x = next_x % N
            next_y = next_y % N
            new_fireball[(next_x,next_y)]+=[[next_x,next_y,m,s,d]]


    # 격자에 이동한 파이어볼 표시
    for key, value in new_fireball.items():
        for v in value:
            i,j,m,s,d = v[0],v[1],v[2],v[3],v[4]
            if lst[i][j]!=0:
                lst[v[0]][v[1]]+=[[i,j,m,s,d]]
            else:
                lst[i][j]=[[i,j,m,s,d]]

    # 한칸에 2개이상의 파이어볼이 있는 칸에서
    fireball_items=list(new_fireball.items())
    sub_fireball = defaultdict(list)

    while fireball_items:
        key,value = fireball_items.pop()

        if len(value)>=2:

            len_new_fireball = len(value)
            new_m, new_s, new_d_jjak, new_d_hol, new_d = 0, 0, 0, 0, []

            for v in value:
                i,j,m,s,d = v[0],v[1],v[2],v[3],v[4]
                new_m+=m
                new_s+=s

                if d%2==0:
                    new_d_jjak+=1

                else:
                    new_d_hol+=1

            if new_m < 5:
                lst[key[0]][key[1]] = 0  # 질량이 0인 파이어볼은 소멸됨.
                del new_fireball[key]
                continue

            new_m = new_m // 5
            new_s = (new_s) // (len(lst[i][j]))

            if new_d_jjak == len(new_fireball[key]) or new_d_hol == len(new_fireball[key]):
                new_d = [0, 2, 4, 6]
            else:
                new_d = [1, 3, 5, 7]


            del new_fireball[key]  # 기존의 위치에 있던 파이어볼은 삭제

            for fly_d in new_d:
                new_fireball[(key[0],key[1])] += [[key[0], key[1], new_m, new_s, fly_d]]


    fires={k:v for k,v in new_fireball.items()}  # dictionary 복사
    cnt+=1


total_m=0
for key,value in fires.items():
    for v in value:
        total_m+=v[2]

print(total_m)
