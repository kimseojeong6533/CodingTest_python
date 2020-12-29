import sys
n=int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(sys.stdin.readline()[:-1])
#
# print(n)
# print(li)



ans=[]
for i in li:
    score=0
    stack = []
    for j in list(i):

        if j!='X':
            stack.append(j)
            score+=len(stack)

        else:
            stack=[]
    ans.append(score)

for i in ans:
    print(i)
