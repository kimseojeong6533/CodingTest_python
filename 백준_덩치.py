from sys import stdin
N = int(stdin.readline())
lst=[]
d=[]
for _ in range(N):
    tmp = tuple(map(int,stdin.readline().split()))
    lst.append(tmp)


for tmp in lst:
    more = [i for i in lst if tmp[0]<i[0] and tmp[1]<i[1]]  # 자기자신의 키와 몸무게 보다 큰 것들만 있는 리스트를 만든다
    d.append(len(more)+1) # 해당 리스트의 길이+1 이 자기자신의 등수가 된다

for i in d:
    print(i, end=' ')

