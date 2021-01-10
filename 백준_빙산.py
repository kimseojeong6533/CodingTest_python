from sys import stdin
import copy
import sys
sys.setrecursionlimit(100000)
row, col = list(map(int,stdin.readline().split()))

lst=[]

for _ in range(row):
    lst.append(list(map(int,stdin.readline().split())))

year=1

direction=[(1,0),(-1,0),(0,1),(0,-1)] # 아래, 위, 오른, 왼

def melting(i,j,new_lst,lst):

    sea=0
    for d in direction:
        new_x = i+d[0]
        new_y = j+d[1]
        if new_x<0 or new_x>=row or new_y<0 or new_y>=col:
            continue
        else:
            if lst[new_x][new_y]==0:
                sea+=1

    if lst[i][j]-sea<0:
        new_lst[i][j] = 0
    else:
        new_lst[i][j]=lst[i][j]-sea

    return

def counting(i,j,memo,cnt):
    if (i,j) in memo or i<0 or i>=row or j<0 or j>=col or new_lst[i][j]==0:
        return

    memo.add((i,j))
    counting(i+1,j,memo,cnt)
    counting(i-1,j,memo,cnt)
    counting(i,j+1,memo,cnt)
    counting(i,j-1,memo,cnt)


while(1):
    new_lst = [[0] * col for _ in range(row)]

    # 매년마다 빙산이 녹는 과정
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 0:
                continue
            melting(i,j,new_lst,lst)

    #print(new_lst)
    #print()

    if lst==new_lst:
        print(0)
        break
    # 빙산이 녹은후 덩어리를 세는 과정
    memo=set()
    cnt=0
    for i in range(row):
        for j in range(col):
            if new_lst[i][j]!=0 and (i,j) not in memo:
                counting(i,j,memo,cnt)
                cnt+=1

    #print(cnt)
    if cnt>=2:
        print(year)
        break
    lst=copy.deepcopy(new_lst)
    year+=1