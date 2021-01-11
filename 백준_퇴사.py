from sys import stdin
from collections import defaultdict
import copy

N=int(stdin.readline())
lst=[]
d=defaultdict(int)
for i in range(N):
    lst.append([i+1]+list(map(int,stdin.readline().split()))+[0])

for i,v in enumerate(lst):
    d[i+1]=v

lst_test=copy.deepcopy(lst)
max_val=0

# BFS 활용
while lst_test:
    d, t, p, plus = lst_test.pop(0)
    if (d+t) > (N+1):
        continue

    plus+=p
    max_val=max(max_val,plus)
    sub=lst[d+t-1:]

    if len(sub)!=0:
        for i in sub:
            if (i[0] + i[1]) <= (N+1):
                lst_test.append([i[0],i[1],i[2],plus])

print(max_val)





