# 메모리 초과(BFS) or 시간초과(중복조합)
# 걍 dp 점화식으로 풀어야 될 듯..
from sys import stdin
#from collections import deque
from itertools import combinations_with_replacement
n,k = list(map(int, stdin.readline().split()))

lst = []
for _ in range(n):
    lst.append(int(stdin.readline()))

lst = list(set(lst))
lst.sort()
q = [x for x in lst if x<=k]
#ans = deque([])

cnt = 0
for i in range(1,k+1):
    for j in combinations_with_replacement(q,i):
        if sum(j) == k:
            cnt+=1
print(cnt)


#
# while q:
#     num = q.popleft()  # 리스트
#     num.sort()
#     if sum(num) == k and num not in ans:
#         ans.append(num)
#
#     elif sum(num)>k:
#         continue
#     else:
#         for i in lst:
#             q.append(num+[i])
#
# print(ans)
# print(len(ans))