from sys import stdin
import sys
sys.setrecursionlimit(100000)

T=int(stdin.readline())

lst=[]
for _ in range(T):
    lst.append(int(stdin.readline()))

#print(lst)

def dp(n,target):
    global cnt
    if n==target:
        cnt+=1
        return

    if n>target:
        return

    dp(n+1,target)
    dp(n+2,target)
    dp(n+3,target)


for i in lst:
    cnt = 0
    dp(1,i)
    dp(2,i)
    dp(3,i)
    print(cnt)