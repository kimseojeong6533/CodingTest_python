from sys import stdin
import sys
N = int(stdin.readline())

lst = []
for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))

answer = sys.maxsize


def dfs(row , col, x, ans1, sub):
    global answer

    if row == 0:
        for k in range(len(lst[row+1])):
            if k == col:
                continue
            dfs(row+1, k, lst[row+1][k], ans1 + lst[row+1][k], sub+[k])

    elif row == N-1:
        for k in range(len(lst[row])):
            if k == col:
                continue
            ans1 += lst[row][k]
            print('마지막 : ', row, col, x, ans1, sub)
            answer = min(answer ,ans1)
        return

    else:
        if row == 1:
            for k in range(len(lst[row+1])):
                if k == col or k in sub:
                    continue
                dfs(row+1, k, lst[row+1][k], ans1 + lst[row+1][k], sub+[k])
        else:
            for k in range(len(lst[row+1])):
                if k == col or k in sub:
                    continue
                dfs(row+1, k, lst[row+1][k], ans1 + lst[row+1][k], sub+[k][1:])

sub = []
for j in range(len(lst[0])):
    dfs(0,j,lst[0][j], lst[0][j], [j])


print(answer)