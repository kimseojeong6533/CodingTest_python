from sys import stdin
T = int(stdin.readline())
answer = []
def func(lst):

    lst.sort(key=lambda x: (x[0]))
    lst2 = [x[1] for x in lst]
    c = lst2[0]
    ans = [c]
    for i in range(1,len(lst2)):
        if c > lst2[i]:
            ans.append(lst2[i])
            c=lst2[i]
    return ans

for _ in range(T):
    N = int(stdin.readline())
    tmp = []
    for _ in range(N):
        tmp.append(tuple(map(int,stdin.readline().split())))
    res = func(tmp)
    answer.append(len(res))


for i in answer:
    print(i)


# def check(a,b):  # 최대한 많은 칸을 방문시켜야
#     move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     cnt = 0
#     que = [(a,b,forest[a][b],0)]
#     visit = [[0]*n for _ in range(n)]
#     eating = forest[a][b]
#
#
#     forest2 = [x for x in forest]
#     while(que):
#         x,y,bamboo = que.pop(0)
#         for d in move:
#             nx = x+d[0]
#             ny = y+d[1]
#
#             if nx>=0 and nx<n and ny>=0 and ny<n and visit[nx][ny]==0 and forest[nx][ny]>bamboo:
#                 visit[nx][ny]=1
#                 eating+=forest[nx][ny]
#                 bamboo = forest[nx][ny]