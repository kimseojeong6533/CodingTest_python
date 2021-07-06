from sys import stdin

move = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
testcase = int(stdin.readline())

lst = []
for _ in range(testcase):
    l = int(stdin.readline())
    x,y = list(map(int,stdin.readline().split()))
    ex,ey = list(map(int,stdin.readline().split()))
    lst.append([l,(x,y),(ex,ey)])


for i in lst:
    l, (x,y), (ex,ey) = i
    #print('l : ',l,' (x,y) : ',x,y,' (ex,ey) : ',ex,ey)
    board = [[0]*l for _ in range(l)]
    board[x][y] = 1
    visit = [[0]*l for _ in range(l)]
    visit[x][y] = 1
    que = [(x,y,0)]
    kahn = []
    while(que):
        a,b,c = que.pop(0)
        #print('(a,b,c) : ',a,b,c)
        if a==ex and b==ey:
            print(c)
            break

        for m in move:
            nx = a+m[0]
            ny = b+m[1]
            if nx>=0 and nx<l and ny>=0 and ny<l and visit[nx][ny]==0:
                que.append((nx,ny,c+1))
                visit[nx][ny] = 1

