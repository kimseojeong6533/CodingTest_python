from sys import stdin
N=int(stdin.readline())  # N : 홀수
lst=[]
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

outsand=0
direction=[(0,-1),(1,0),(0,1),(-1,0)]  # 서-남-동-북 (토네이도이동)


# d==0 (서쪽일 때)
sand_direction=[
                [(-2,0),(2,0),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1),(0,-2)],  # d=0
                [(0,-2),(0,2),(0,-1),(0,1),(1,-1),(1,1),(-1,-1),(-1,1),(2,0)],   # d=1
                [(-2,0),(2,0),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1),(0,2)],   # d=2
                [(0,-2),(0,2),(0,-1),(0,1),(1,-1),(1,1),(-1,-1),(-1,1),(-2,0)]   # d=3

                ]
sand_ratio=[2, 2, 7, 7, 10,10,1,1,5]
                # 2%,   2%,    7%     7%     10%    10%    1%      1%  5%
#
# # d==1 (남쪽일 때)
# sand_direction=[(0,-2),(0,2),(0,-1),(0,1),(1,-1),(1,1),(-1,-1),(-1,1),(2,0)]
#
# # d==2 (동쪽일 때)
# sand_direction=[(-2,0),(2,0),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1),(0,2)]
#                 # 2%,   2%,    7%     7%     10%    10%    1%      1%  5%
#
# # d==3 (북쪽일 때)
# sand_direction=[(0,-2),(0,2),(0,-1),(0,1),(1,-1),(1,1),(-1,-1),(-1,1),(-2,0)]
#                 # 2%,   2%,    7%     7%     10%    10%    1%      1%  5%



# 이동시작점
x,y = N//2, N//2

# 초기방향
d=0

# 초기 스피드(이동거리)
default_s=1

while(1):

    if x==1 and y==1:
        break
    print(outsand)

    # (x,y)가 반시계방향으로 움직임
    dist=1
    while(dist<=default_s):   # 2번동안 이동거리는 같지만 방향은 계속 바뀜
        s=0
        #next_x,next_y = x,y

        while(s<default_s):  # s(이동거리)만큼 next_x를 움직임
            next_x = x+direction[d][0]  # 이동할 자리(y) , 인덱스가 바깥으로 나가지 않음
            next_y = y+direction[d][1]


            print('next_x : ',next_x,'  next_y : ',next_y)
            # 각 격자에 모래가 흩날리는 비율 계산
            for sand_d,sand_r in zip(sand_direction[d],sand_ratio)  :
                fly_x = next_x+sand_d[0]
                fly_y = next_y+sand_d[1]

                if fly_x<0 or fly_x>=N or fly_y<0 or fly_y>=N:
                    outsand += round(lst[next_x][next_y]*sand_r/100)
                else:
                    lst[fly_x][fly_y] += round((lst[next_x][next_y]*sand_r)/100)

            # a자리의 모래양 계산
            a_x=next_x+direction[d][0]
            a_y=next_y+direction[d][1]
            if a_x<0 or a_x>=N or a_y<0 or a_y>=N:
                outsand += (lst[next_x][next_y]*55)/100  # 나머지는 55프로

            else:
                lst[a_x][a_y] += round((lst[next_x][next_y]*55)/100)


            s += 1
            x, y = next_x, next_y

        d+=1
        if d >= 4:
            d = 0

        #print('x,y : ', x, y)

        dist+=1
        default_s += 1  # 거리 +1






#print(outsand)
#print(lst)

