from sys import stdin
N = int(stdin.readline())

lst = []
for _ in range(N):
    tmp = list(map(int,stdin.readline().split()))
    lst.append(tmp)

lst.sort(key=lambda x:(x[1],x[0]))
end = lst[0][1]
result = 1
for i in range(1,N):
    if lst[i][0]>=end:
        result += 1
        end=lst[i][1]
print(result)