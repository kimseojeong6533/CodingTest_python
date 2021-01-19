from sys import stdin

T=int(stdin.readline())

lst=[]
for _ in range(T):
    lst.append(list(map(int,stdin.readline().split(','))))

for a,b in lst:
    print(a+b)