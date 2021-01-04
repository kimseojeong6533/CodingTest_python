# 시간초과

from sys import stdin

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C = list(map(int, stdin.readline().split()))

board = []
for _ in range(R):
    board.append(list(stdin.readline())[:-1])

answer=1

def dfs(x,y,ans):
    global answer
    answer=max(answer,ans)  # 함수 바깥의 변수를 사용하기위해서는 [global 변수이름]을 해주어야 한다.

    for d in direction:
        nx=x+d[0]
        ny=y+d[1]

        if (0<=nx<R) and (0<=ny<C) and (board[nx][ny] not in alphas):

            alphas.append(board[nx][ny])
            print(alphas)
            dfs(nx,ny,ans+1)
            alphas.remove(board[nx][ny])

alphas=[board[0][0]]
dfs(0,0,answer)
print(answer)


'''
내가한 풀이 : (틀림)
from sys import stdin

R, C = list(map(int, stdin.readline().split()))

board = []
for _ in range(R):
    board.append(list(stdin.readline())[:-1])

visit = [[1] * C for _ in range(R)]

alphas = [board[0][0]]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(i, j,alphas):
    #print(i,j,board[i][j])
    if i < 0 or i >= R or j < 0 or j >= C or visit[i][j]!=1:
        return

    for d in direction:
        new_i = i + d[0]
        new_j = j + d[1]

        if new_i < 0 or new_i >= R or new_j < 0 or new_j >= C or board[new_i][new_j] == board[i][j] or visit[new_i][new_j]!=1 or board[new_i][new_j] in alphas:
            continue

            #if board[new_i][new_j] != board[i][j]:
            #print(i,j,new_i,new_j)
        if board[new_i][new_j] == 'D':
            print(alphas)
            print(visit)


        visit[new_i][new_j]+=visit[i][j]
        dfs(new_i, new_j,alphas+[board[new_i][new_j]])
        # else:
        #     return

    else:
        return


(x, y) = (0, 0)
for d in direction:
    n_x = x + d[0]
    n_y = y + d[1]
    visit[n_x][n_y]+=visit[x][y]
    dfs(n_x, n_y,alphas+[board[n_x][n_y]])

print(visit)
answer = sum(visit, [])  # extend
print(max(answer))



'''