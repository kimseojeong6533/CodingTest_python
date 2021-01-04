from sys import stdin
from collections import defaultdict
T=int(stdin.readline())

lst=[]
for _ in range(T):
    #lst.append(stdin.readline()[:-1])
    lst.append(input())

#print(lst)
ans=[]
for st in lst:
    d = defaultdict(int)
    for j in st:
        d[j]+=1

    sub=[key for key,val in d.items() if val%2!=0]
    sub.sort()
    if len(sub)==0:
        ans.append('Good')
    else:
        ans.append(''.join(sub))
#print(ans)
for i in range(len(ans)):
    print('#{0} {1}'.format(i+1,ans[i]))

