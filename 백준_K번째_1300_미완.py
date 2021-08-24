from sys import stdin


N = int(stdin.readline())
K = int(stdin.readline())

A = [i*j for i in range(1, N+1) for j in range(1,N+1)]
A = []




for i in range(1,min(1000000000,N**2)):
    if i == k:
        print(i)





