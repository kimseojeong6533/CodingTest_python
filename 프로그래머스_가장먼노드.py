from collections import defaultdict
from collections import deque


def solution(n, edge):
    d = defaultdict(list)
    memo = set()
    ans = defaultdict(int)

    for i in edge:
        d[i[0]] += [i[1]]
        d[i[1]] += [i[0]]

    q = deque([(1, 1)])
    while q:
        node, cnt = q.popleft()
        # print(node,cnt)

        if node in memo:
            continue
        memo.add(node)
        ans[cnt] += 1
        cnt += 1
        for j in d[node]:
            if j in memo:
                continue
            q.append((j, cnt))

    return ans[sorted(ans.keys())[-1]]

n=6
vertex=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))