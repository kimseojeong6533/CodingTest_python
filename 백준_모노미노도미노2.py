from sys import stdin

N = int(stdin.readline())
lst = []
for _ in range(N):
    a = tuple(map(int, stdin.readline().split()))
    lst.append(a)

# (t, x, y) -> t=1 : 1x1블록을 (x,y)에 넣음
#           -> t=2 : 1x2블록을 (x,y), (x,y+1)에 놓음
#           -> t=3 : 2x1블록을 (x,y), (x+1,y)에 놓음

domino = [[0,0,0,0,1,1,2,2,2,2],[0,0,0,0,1,1,2,2,2,2],[0,0,0,0,1,1,2,2,2,2],[0,0,0,0,1,1,2,2,2,2],[3,3,3,3,-1,-1,-1,-1,-1,-1],[3,3,3,3,-1,-1,-1,-1,-1,-1],[3,3,3,3,-1,-1,-1,-1,-1,-1],[3,3,3,3,-1,-1,-1,-1,-1,-1],[3,3,3,3,-1,-1,-1,-1,-1,-1],[3,3,3,3,-1,-1,-1,-1,-1,-1]]
#print(domino)

for i in lst:
    t, x, y = i
    if t==1:
        nx, ny = x, y
        flag1 = True
        flag2 = True
        while(1):
            if domino[nx][ny] != 9 and nx <= 9:   # 빨간보드로
                nx+=1


        if flag1:

q



        nx, ny = x, y
        while domino[nx][ny] != 9 and ny <= 9:   # 파란보드로
            ny+=1

    elif t==2:

    else:
