from sys import stdin
from collections import defaultdict
N, K = list(map(int, stdin.readline().split()))


d = defaultdict(int)
lst=[]
for _ in range(N):
    lst.append(int(stdin.readline()))

lst.sort(reverse=True)
for i in lst:
    n, r = divmod(K,i)
    if n==0:
        continue
    d[i]=n
    K = K - n*i
#print(lst)
#print(d)
print(sum(d.values()))