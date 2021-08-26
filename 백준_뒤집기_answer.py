from sys import stdin

S = stdin.readline()[:-1]
# S = "01"*500000
lst = [0,0]

f = S[0]

# 문자열의 0과 1로 이루어진 연속된 덩이수를 세서, 수가 더 적은 쪽을 출력
if len(S)>1:
    for i in S[1:]:
        if f != i:
            lst[int(f)] += 1
            f = i
    lst[int(f)] += 1
    if lst[0] > lst[1]:
        print(lst[1])
    else:
        print(lst[0])

else:
    print(0)


