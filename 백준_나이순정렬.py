from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
d=defaultdict(tuple)
for i in range(1,n+1):
    d[i] = (stdin.readline().split())
    d[i][0] = int(d[i][0])

ans = sorted(d.items(), key = lambda x: (x[1][0],x[0]))
#print(ans)
for i in ans:
    print(i[1][0], i[1][1])