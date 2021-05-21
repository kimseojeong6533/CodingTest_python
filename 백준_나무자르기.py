from sys import stdin

N, M = list(map(int,stdin.readline().split()))
trees = list(map(int,stdin.readline().split()))

left = 0
right = max(trees)
ans = -1

while(left<=right):
    mid = (left+right)//2
    sub = sum([i-mid for i in trees if i > mid])
    if sub >= M:
        left = mid + 1
        ans = mid
    elif sub < M:
        right = mid - 1

print(ans)



