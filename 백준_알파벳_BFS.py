from sys import stdin

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C = list(map(int, stdin.readline().split()))

board = []
for _ in range(R):
    board.append(list(stdin.readline())[:-1])

answer=1
alphas=board[0][0]  # alphas : str
def bfs(x,y,alphas):
    q=[(x,y,alphas)]
    global answer

    while q:
        i,j,alphas_lst=q.pop()  # ?? pop(0)가 아니라 pop()을 하니까 맞았따... ㅋㅋㅋ 뭐징

        for d in direction:
            nx=i+d[0]
            ny=j+d[1]

            if (0<=nx<R) and (0<=ny<C) and (board[nx][ny] not in alphas_lst):
                q.append((nx,ny,alphas_lst+board[nx][ny]))
                answer=max(answer,len(alphas_lst)+1)


bfs(0,0,alphas)
print(answer)
