from sys import stdin
from itertools import permutations
import sys
N=int(stdin.readline())

lst = list(map(int, stdin.readline().split()))

lst_opr = list(map(int, stdin.readline().split()))   # 길이 : 4

opp=['+', '-', '*', '/']
d = {k : v for k, v in zip(opp,lst_opr)}

st=''
for k, v in d.items():
    st += (k*v)


c=list(set(permutations(st, sum(d.values()))))
print(len(c))

d= list(permutations(st, sum(d.values())))
print(len(d))
print()

ans_max = -sys.maxsize
ans_min = sys.maxsize
lst_0 = lst.pop(0)


for i in c:
    sub = lst_0
    for p, n in zip(i, lst):
        #print(p,n)
        if p == '/':
            if sub<0:
                sums = -eval(str(-sub) + '//' + str(n))
            else:
                sums = eval(str(sub) + '//' + str(n))
        else:
            sums = eval(str(sub) + p + str(n))
        sub = sums
    #print('sums : ',sums)
    ans_max = max(ans_max, sums)
    ans_min = min(ans_min, sums)


print(ans_max)
print(ans_min)

