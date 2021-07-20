from sys import stdin


n = int(stdin.readline())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
forest = []

for _ in range(n):
    sub = list(map(int,stdin.readline().split()))
    forest.append(sub)


# dfs로 풀어보자 + memoization?
res = []
def check(a,b,kahn,bamboo,v,lst):

    lst.append(kahn)
    for d in move:
        x = a + d[0]
        y = b + d[1]
        v2 = [p[:] for p in v]  # 2차원 배열 복사

        if x>=0 and x<n and y>=0 and y<n and forest[x][y]>bamboo and v2[x][y]==0:
            if ans[x][y] == 0:
                v2[x][y] = 1
                lst.append(check(x,y,kahn+1,forest[x][y],v2,lst))
            else:
                lst.append(kahn+ans[x][y])

    return max(lst)


visit = [[0]*n for _ in range(n)]

ans = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):

        sub = []
        sub.append(check(i,j,1,forest[i][j],visit,[]))
        ans[i][j] = max(sub)

answer = [y for x in ans for y in x]
#print(ans)
print(max(answer))