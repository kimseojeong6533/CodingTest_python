from itertools import combinations_with_replacement
k=10
cnt = 0
for i in range(1,11):
    for c in combinations_with_replacement([1,3,5],i):
        if sum(c)==k:
            cnt+=1
            print(c, end = ' ')
    print(cnt)