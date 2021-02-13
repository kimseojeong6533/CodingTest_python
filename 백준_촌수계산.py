from sys import stdin
from collections import defaultdict

d_ps = defaultdict(list)
d_sp = defaultdict(list)
n = int(stdin.readline())

a, b = list(map(int, stdin.readline().split()))

m = int(stdin.readline())

lst = []
for _ in range(m):
    x, y = list(map(int, stdin.readline().split()))
    d_ps[x] += [y]
    d_sp[y] += [x]
# print(d_ps)
# print(d_sp)
# print()


# a, b의 부모들에 대한 리스트를 작성
a_lst = [a]
b_lst = [b]

x, y = a, b
while(1):
    if d_sp.get(x):
        for i in d_sp[x]:
            a_lst.append(i)
            x = i
    else:
        break

while(1):
    if d_sp.get(y):
        for i in d_sp[y]:
            b_lst.append(i)
            y = i
    else:
        break
root = 0

flag = False

for i in a_lst:
    for j in b_lst:
        if i == j:            # 친척인지, 남인지 판별 -> 친척이면 flag = True, 남이면 False
            root = i          # 친척일 때에는, a,b의 부모리스트에 둘다 존재하면서 가장 먼저 찾은 값이 a,b의 root값이 됨 -> root값을 기준으로 자식노드마다의 높이를 세서 합하면 촌수가 됨.
            flag = True
            break
    if flag:
        break
if flag:            # 친척인 관계일 때,
    def dfs(i):
        if d_ps.get(i):
            for j in d_ps[i]:
                node_lst[j] = node_lst[i] + 1
                if j == a or j == b:
                    flag_lst.append(j)
                dfs(j)

        else:
            return


    node_lst = [0] * (n + 1)
    node_lst[0] = '?'
    flag_lst = []
    if root == a or root == b:
        flag_lst.append(root)

    dfs(root)
    #print(node_lst)
    if sorted(flag_lst) == sorted([a, b]):
        print(node_lst[a] + node_lst[b])


else:  # 남일 때
    print(-1)


