from sys import stdin
import sys
from collections import deque

n, k = list(map(int, stdin.readline().split()))

lst = []
for _ in range(n):
    lst.append(int(stdin.readline()))

lst = list(set(lst))
lst.sort()
coins = 0

q = deque([])
check = [0]*(k+1)

for i in lst:
    if i <= k:
        q.append([i,1])
        check[i]=1

while q:
    num, cnt = q.popleft() # 리스트

    if num == k:
        coins = cnt
        break

    for i in lst:
        if num+i > k:
            continue
        if check[num+i] == 0:
            q.append([num+i,cnt+1])
            check[num + i] = 1

if coins != 0:
    print(coins)
else:
    print(-1)

# def dp(x):
#     global coins
#
#     if sum(x) == k:
#         x.sort()
#         if x not in ans:
#             ans.append(x)
#             coins = min(coins, len(x))
#             return
#         else:
#             return
#
#     if sum(x) > k:
#         return
#
#     for j in lst:
#         dp(x+[j])
#
#
# for i in lst:
#     dp([i])
#
# if coins == sys.maxsize:
#     print(-1)
# else:
#     print(coins)
#
# print()
# for i in ans:
#     print(i)
