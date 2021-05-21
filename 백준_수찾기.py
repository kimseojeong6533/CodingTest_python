from sys import stdin

N = int(stdin.readline())
a = list(map(int,stdin.readline().split()))

M = int(stdin.readline())
b = list(map(int,stdin.readline().split()))

ans = []
for num in b:
    if num in a:
        ans.append(1)
    else:
        ans.append(0)
for i in ans:
    print(i)