from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

N=int(stdin.readline())

lst=[]
for _ in range(N-1):
    lst.append(tuple(map(int,stdin.readline().split())))

d=defaultdict(list)
ans=defaultdict(int)

for i in lst:              # 부모 : 자식을 리스트로 된 사전으로 만들어 그래프를 생성
    d[i[0]]+=[i[1]]
    d[i[1]]+=[i[0]]
print(d)

memo=set()           # append보다는 add가 빠름
def findings(i,memo):    # 1번노드부터 부모 -> 자식순으로 내려가면서 해당 자식을 키로,그 자식의 부모를 값으로하여 사전(ans)으로 기록, memo는

    memo.add(i)
    while d.get(i):
        a = d[i].pop(0)
        if a in memo:
            continue
        ans[a] = i          # 자식(key) : 부모(value)
        findings(a, memo)

findings(1,memo)
print(ans)
for i in sorted(ans.items(),key=lambda x:x[0]):
    print(i[1])
