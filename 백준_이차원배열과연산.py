from sys import stdin
from collections import Counter
r, c, n = list(map(int,stdin.readline().split()))

A = []
for _ in range(3):
    A.append(list(map(int,stdin.readline().split())))


sec=0
# print('A : ', A)
#print('r,c,k : ',r,c,n)
# print()

while(1):
    row = len(A)
    col = len(A[0])
    # print('A[r-1][c-1] : ', A[r-1][c-1], 'n : ', n )
    #print('A ; ', A)
    if len(A) >= r and len(A[0]) >= c:
        if A[r-1][c-1] == n:
            print(sec)
            break
    sec += 1
    if sec > 100:
        sec = -1
        print(sec)
        break

    tot = []
    if row >= col:  # R연산

        longest = -1
        for i in range(len(A)):
            sub = []
            for k,v in Counter(A[i]).items():
                if k==0:
                    continue
                sub.append([k,v])

            longest = max(longest, len(sub)*2)
            if sub:

                sub.sort(key = lambda x: (x[1], x[0]))


                sub2 = []
                for a,b in sub:
                    sub2.extend([a,b])
                tot.append(sub2)

        for i in range(len(tot)):
            if len(tot[i]) < longest:
                tot[i] += [0]*(longest-len(tot[i]))

        #print('1 - tot : ', tot)

        A = []
        for i in range(len(tot)):
            sub = []
            for j in range(len(tot[i])):
                sub.append(tot[i][j])
            A.append(sub)
    else:         # C연산
        longest = -1

        # 행열 변환 (A -> A2)
        A2 = []
        for i in range(len(A[0])):
            sub=[]
            for j in range(len(A)):
                sub.append(A[j][i])
            A2.append(sub)

        # 계산
        longest = -1
        for i in range(len(A2)):
            sub = []
            for k, v in Counter(A2[i]).items():
                if k == 0:
                    continue
                sub.append([k, v])
            longest = max(longest, len(sub)*2)

            if sub:
                sub.sort(key = lambda x: (x[1], x[0]))

                sub2 = []
                for a, b in sub:
                    sub2.extend([a, b])
                tot.append(sub2)

        for i in range(len(tot)):
            if len(tot[i]) < longest:
                tot[i] += [0] * (longest - len(tot[i]))
        #print('2 - tot : ', tot)

        # tot -> A 복사
        A = []
        for i in range(len(tot[0])):
            sub=[]
            for j in range(len(tot)):
                sub.append(tot[j][i])
            A.append(sub)

