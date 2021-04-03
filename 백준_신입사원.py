from sys import stdin
T = int(stdin.readline())
answer = []
def func(lst):

    lst.sort(key=lambda x: (x[0]))
    lst2 = [x[1] for x in lst]
    c = lst2[0]
    ans = [c]
    for i in range(1,len(lst2)):
        if c > lst2[i]:
            ans.append(lst2[i])
            c=lst2[i]
    return ans

for _ in range(T):
    N = int(stdin.readline())
    tmp = []
    for _ in range(N):
        tmp.append(tuple(map(int,stdin.readline().split())))
    res = func(tmp)
    answer.append(len(res))


for i in answer:
    print(i)