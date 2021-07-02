from sys import stdin
import heapq

N = int(stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(stdin.readline()))

heapq.heapify(lst)

if len(lst)>2:
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    a += b
    heapq.heappush(lst,a)
    while(lst):
        b=heapq.heappop(lst)
        c=heapq.heappop(lst)
        a+=(b+c)
        if lst:
            heapq.heappush(lst,b+c)
        else:
            print(a)
            break
elif len(lst)==2:
    print(sum(lst))

else:
    print(0)

