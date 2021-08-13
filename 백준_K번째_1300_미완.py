from sys import stdin


N = int(stdin.readline())
K = int(stdin.readline())

A = [i*j for i in range(1, N+1) for j in range(1,N+1)]
A.sort()
print(A[K-1])





