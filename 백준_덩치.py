from sys import stdin

N = int(stdin.readline())
lst=[]
for _ in range(N):
    lst.append(tuple(map(int,stdin.readline().split())))

print(lst)

wet = [x[0] for x in lst]
het = [x[1] for x in lst]
wet.sort(reverse=True)
het.sort(reverse=True)
print(wet)
print(het)
ans = []
sub=0
for i, j in zip(range(len(wet)),range(len(het))):
    if (wet[i],het[j]) in lst:
        ans.append(i)
        sub=i
    else:
        ans.append(sub+1)
print(ans)

