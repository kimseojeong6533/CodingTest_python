from sys import stdin
import sys
sys.setrecursionlimit(100000)
n = int(stdin.readline())
lst = []
for _ in range(n):
    sub = list(map(int,stdin.readline().split()))
    lst.append(sub)

for i in range(1,len(lst)):
    for j in range(i+1):
        if j==0:
            lst[i][j] += lst[i-1][j]

        elif j==i:
            lst[i][j] += lst[i-1][j-1]

        else:
            lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])
#print(lst)
print(max(lst[-1]))






#print(lst)
#
# val = lst[0][0]
# cnt = -1
#
# def dp(v, x, y):
#
#     global cnt
#     if x == len(lst):
#         cnt = max(cnt,v)
#         return
#
#     else:
#         dp(v+lst[x][y], x + 1, y)
#         dp(v+lst[x][y], x + 1, y+1)
#
# for i in range(len(lst[1])):
#     dp(val,1,i)
#
# print(cnt)