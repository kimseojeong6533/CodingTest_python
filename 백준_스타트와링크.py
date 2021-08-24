from sys import stdin
import sys
from collections import defaultdict


answer = sys.maxsize
N = int(stdin.readline())
lst = []


for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

std = list(range(0,N))
d = defaultdict(int)

def ability_cnt(res1):
    r = 0
    for a in range(len(res1)-1):
        for b in range(a+1,len(res1)):
            r += lst[res1[a]][res1[b]] + lst[res1[b]][res1[a]]
    return r

# dfs로 경우의수를 구함
def dfs(sub):
    global answer

    if (len(sub) == (N//2)):
        sub2 = [j for j in std if j not in sub]
        sub.sort()
        sub2.sort()
        if tuple(sub) not in d and tuple(sub2) not in d:

            # 스타트팀(sub), 링크팀(sub2)
            c1 = ability_cnt(list(sub))
            c2 = ability_cnt(list(sub2))
            #print(sub,sub2)
            d[tuple(sub)] = abs(c1-c2)
            d[tuple(sub2)] = abs(c1-c2)
            # answer = min(answer,abs(c1-c2))
        return

    for k in range(0,N):
        if k in sub:
            continue
        dfs(sub+[k])
    return

for i in range(0,N//2):
    dfs([i])

# print()
#print(d)
# print(len(d))
print(min(d.values()))