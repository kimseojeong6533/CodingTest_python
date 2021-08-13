from sys import stdin
# 11004번 K번째 수 문제

N, K = list(map(int, stdin.readline().split()))
lst = list(map(int, stdin.readline().split()))

lst.sort()
print(lst[K-1])