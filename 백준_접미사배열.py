from sys import stdin

S = stdin.readline()[:-1]

lst = []
for i in range(len(S)):
    lst.append(S[i:])
for i in sorted(lst):
    print(i)