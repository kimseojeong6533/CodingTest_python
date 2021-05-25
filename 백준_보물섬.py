from sys import stdin
r,c = list(map(int,stdin.readline().split()))
dire = [(1,0),(0,1),(-1,0),(0,-1)]

zido = []
for _ in range(r):
    zido+=[list(stdin.readline())[:-1]]

land = []
for i in range(r):
    for j in range(c):
        if zido[i][j]=='L':
            land.append((i,j))

def find_treasure(l1,v):
    # 최단거리 중, 가장 큰 값 구하기

    (x1,y1) = l1

    q = [(x1,y1)]
    v[x1][y1]=1
    while(q):
        (x,y) = q.pop(0)

        for d in dire:
            nx = x+d[0]
            ny = y+d[1]

            if nx>=0 and nx<r and ny>=0 and ny<c and v[nx][ny]==0 and zido[nx][ny]=='L':
                v[nx][ny]=v[x][y]+1
                q.append((nx,ny))
    res = 0
    for p in v:
        res = max(res,max(p))

    # res = max([max(x) for x in v])  # 2차원 배열에서 가장 큰 값 찾기
    return res-1

ans = 0
for l in range(len(land)):
    visit = [[0] * c for _ in range(r)]
    ans = max(ans,find_treasure(land[l],visit))
print(ans)