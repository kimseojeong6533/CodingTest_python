from sys import stdin
from collections import defaultdict

N, M = list(map(int,stdin.readline().split()))
d = defaultdict(lambda:0)

for _ in range(N):
    d[stdin.readline()[:-1]] +=1

for _ in range(M):
    d[stdin.readline()[:-1]] += 1

answer = [k for k,v in d.items() if v>=2]
print(len(answer))
answer.sort()
for i in answer:
    print(i)