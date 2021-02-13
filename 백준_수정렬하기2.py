from sys import stdin

N = int(stdin.readline())
lst = []
lst = [int(stdin.readline())for _ in range(N)]
lst.sort()
for i in lst:
    print(i)