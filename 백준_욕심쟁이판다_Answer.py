from sys import stdin

n = int(stdin.readline())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
forest = []

for _ in range(n):
    sub = list(map(int,stdin.readline().split()))
    forest.append(sub)


def check(a,b):

    if visit[a][b] > 0:
        return visit[a][b]

    visit[a][b] = 1
    for m in move:
        x = a + m[0]
        y = b + m[1]
        if x>=0 and x<n and y>=0 and y<n and forest[x][y] > forest[a][b]: # 칸 인덱스를 이탈하거나, 이동한 칸이 이전칸의 대나무수 보다 적거나 같으면 리턴
            visit[a][b] = max(visit[a][b], check(x, y) + 1)
    return visit[a][b]


visit = [[0]*n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, check(i,j))  # 해당 칸(i,j)에서 이동할 수 있는 최대값을 visit에 넣음
        #print(visit)
print(answer)
