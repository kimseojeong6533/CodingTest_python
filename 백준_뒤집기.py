from sys import stdin

#S = stdin.readline()[:-1]
S = "01"*500000

# 1과 0의 연속된 덩이수를 구한다
# 연속된 덩이수가 작은 것부터 바꾼다
# 1 또는 0으로 가득찬 문자열이 될때까지 위 반복

sub = len(S)
cnt = 0
while (1):
    if S == '1' * sub or S == '0' * sub:
        break

    if len(S) > 1:
        lst = [0,0]

        f = S[0]
        for i in S[1:]:
            if f != i:
                lst[int(f)] += 1
                f = i
        lst[int(f)] += 1

    if lst[1] > lst[0]:  # 0 -> 1로 바꿔

        start, end = -1, -1
        for i, j in enumerate(S):
            if j == '0' and start == -1:
                start = i
                continue
            if j == "0" and start >= 0 and i == (len(S) - 1):
                end = i
                break

            if j == '1' and start >= 0:
                end = i - 1
                break

        tmp = '1' * (end - start + 1)
        if end == len(S) - 1:
            S = S[:start] + tmp
        else:
            S = S[:start] + tmp + S[end + 1:]

    else:
        start, end = -1, -1
        for i, j in enumerate(S):
            if j == '1' and start == -1:
                start = i
                continue
            if j == "1" and start >= 0 and i == (len(S) - 1):
                end = i
                break

            if j == '0' and start >= 0:
                end = i - 1
                break

        tmp = '0' * (end - start + 1)
        if end == len(S) - 1:
            S = S[:start] + tmp
        else:
            S = S[:start] + tmp + S[end + 1:]
    # print(S)
    # print()
    cnt += 1

print(cnt)



