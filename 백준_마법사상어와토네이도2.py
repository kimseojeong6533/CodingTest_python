# Simulation 문제

from sys import stdin
N=int(stdin.readline())  # N : 홀수
lst=[]
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

outsand=0
direction=[(0,-1),(1,0),(0,1),(-1,0)]  # 서-남-동-북 (토네이도이동)


# d==0 (서쪽일 때)
sand_direction=[
                [(-2,0),(2,0),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1),(0,-2)],  # d=0 (서)
                [(0,-2),(0,2),(0,-1),(0,1),(1,-1),(1,1),(-1,-1),(-1,1),(2,0)],   # d=1 (남)
                [(-2,0),(2,0),(-1,0),(1,0),(-1,1),(1,1),(-1,-1),(1,-1),(0,2)],   # d=2 (동)
                [(0,-2),(0,2),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1),(-2,0)]   # d=3 (북)

                ]
sand_ratio=[2, 2, 7, 7, 10,10,1,1,5]

# 이동시작점
x,y = N//2, N//2

# 거리
distance=1

# 초기방향값
d=0


flag=True

while flag:

    dist_cnt=1

    while flag and (dist_cnt <= 2):
        dist = 1
        while flag and (dist <= distance):

            next_x = x + direction[d][0]  # 토네이도가 이동할 자리(y) , 인덱스가 바깥으로 나가지 않음
            next_y = y + direction[d][1]
            mov_sand=0

            for sand_d,sand_r in zip(sand_direction[d],sand_ratio):

                fly_x = next_x+sand_d[0]
                fly_y = next_y+sand_d[1]
                mov_sand += ((lst[next_x][next_y] * sand_r) // 100)
                if fly_x<0 or fly_x>=N or fly_y<0 or fly_y>=N:       # 인덱스밖을 벗어나면
                    outsand += ((lst[next_x][next_y]*sand_r)//100)

                else:                                                # 인덱스밖을 벗어나지 않으면
                    lst[fly_x][fly_y] += ((lst[next_x][next_y]*sand_r)//100)


            remain_sand = lst[next_x][next_y] - mov_sand  # 원래모래 - 이동한 모래 = 이동하지않은 남은 모래의 양
            # a자리의 모래양 계산
            a_x=next_x+direction[d][0]
            a_y=next_y+direction[d][1]


            if a_x<0 or a_x>=N or a_y<0 or a_y>=N:
                outsand += remain_sand

            else:                                        # 인덱스밖을 벗어나지 않으면
                lst[a_x][a_y] += remain_sand


            x, y = next_x, next_y

            if x == 0 and y == 0:
                flag=False
                break

            dist+=1

        d+=1
        if d>=4:
            d=0
        dist_cnt+=1

    distance+=1


print(outsand)