from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
lst = list(map(int,stdin.readline().split()))
d = defaultdict(int)

answer = []
for i in lst:
    if i in d:
        continue
    else:
        answer.append(i)
        d[i] = 1

for i in sorted(answer):
    print(i, end = ' ')

