from sys import stdin

a, b = list(map(int, stdin.readline().split()))

arr = [x for x in range(1, a + 1)]
ans = [0] * a

ind, cnt = 0, 0

answer = []
while (arr != ans):

    if arr[ind] != 0:
        cnt += 1

    if cnt == b:
        answer.append(arr[ind])
        arr[ind] = 0
        cnt = 0

    ind += 1
    if ind >= a:
        ind = 0

print('<',end='')
for i in range(len(answer)):
    if i==len(answer)-1:
        print(answer[i],end='>')
    else:
        print(answer[i], end=', ')