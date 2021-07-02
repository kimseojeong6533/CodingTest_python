from sys import stdin

dire = [(1,0),(-1,0),(0,1),(0,-1)]
N,M,K = list(map(int,stdin.readline().split()))


lst = []
for _ in range(N):
    lst.append(list(stdin.readline())[:-1])

print(lst)
def dfs(x,y,wall,v):
    v[x][y]=1

    q = [(x,y,wall)]
    print('v : ',v)
    while(q):
        i,j,cnt = q.pop(0)
        for d in dire:
            nx = i + d[0]
            ny = j + d[1]

            if nx==(N-1) and ny==(M-1):
                return v[nx][ny]

            if nx>=0 and nx<N and ny>=0 and ny<M and v[nx][ny]==0 and lst[nx][ny]=='0':
                v[nx][ny] = v[i][j]+1
                q.append((nx,ny,cnt))

            if nx>=0 and nx<N and ny>=0 and ny<M and v[nx][ny]==0 and lst[nx][ny]=='1' and cnt<K:
                v[nx][ny] = v[i][j] + 1
                q.append((nx,ny,cnt+1))


visit = [[0]*M for _ in range(N)]

ans = []
ans.append(dfs(0,0,0,visit))

print(min(ans)-1)
