from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

N, Q = list(map(int,stdin.readline().split()))

lst=[]
for _ in range(2**N):
    lst.append(list(map(int,stdin.readline().split())))

L_list = list(map(int,stdin.readline().split()))


# 파이어스톰을 시전
for L in L_list:
    lst2 = [[0] * (2 ** N) for _ in range(2 ** N)]  # 회전후의 얼음판을 담음
    if L>0:
        # 2**L x 2**L 부분격자로 나누고 90도 회전
        part_len=2**L
        row, col = 0, 0

        while(1):
            if row+part_len>2**N:
                break

            for i in range(row,row+part_len):
                for j in range(col,col+part_len):
                    #print(i,j,' / ',j+row-col,row+part_len+col-1-i)
                    lst2[j+row-col][row+part_len+col-1-i] = lst[i][j]

            col+=part_len
            if col>=2**N:
                col=0
                row+=part_len


    else: # L == 0 이면 회전하지 않음 (1x1부분격자이므로)
        for i in range(2**N):
            for j in range(2**N):
                lst2[i][j]=lst[i][j]

    lst3=[[0]*(2**N) for _ in range(2**N)]

    # 얼음이 있는칸 3개이상과 인접하지않은 칸에 얼음양 -1
    direction=[(1,0),(-1,0),(0,1),(0,-1)]

    for i in range(2**N):
        for j in range(2**N):
            if lst2[i][j]>0:
                cnt=0
                for d in direction:
                    new_x=i+d[0]
                    new_y=j+d[1]
                    if new_x<0 or new_x>=2**N or new_y<0 or new_y>=2**N or lst2[new_x][new_y]<=0:
                        continue
                    cnt+=1

                if cnt<3:
                    lst3[i][j]=lst2[i][j]-1
                else:
                    lst3[i][j]=lst2[i][j]

    lst=[[0]*(2**N) for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            lst[i][j]=lst3[i][j]


# 칸에서 남아있는 얼음의 합 구하기
ice_sum=0
for x in lst:
    ice_sum += sum(x)

print(ice_sum)

# 남아있는 얼음 중 가장 큰 덩어리찾기 (dfs)
d=defaultdict(int)
visit=[[0]*(2**N) for _ in range(2**N)]


def find_dungeori(i,j,d_num):
    if i<0 or i>=2**N or j<0 or j>=2**N or lst[i][j]<=0 or visit[i][j]==1:
        return

    visit[i][j]=1
    d[d_num]+=1                    # 각 덩어리의 번호 : d_num
    find_dungeori(i + 1, j, d_num)
    find_dungeori(i - 1, j, d_num)
    find_dungeori(i, j+1, d_num)
    find_dungeori(i, j-1, d_num)


d_num=0
for i in range(2**N):
    for j in range(2**N):
        if visit[i][j]==1 or lst[i][j]<=0:
            continue

        d[d_num]=0
        find_dungeori(i,j,d_num)
        d_num+=1


# 가장 큰 덩어리의 칸개수 계산
if d.values():
    biggest_kan = sorted(d.values(), reverse=True)[0]  # value를 기준으로 sort
    print(biggest_kan)

else:
    print(0)
