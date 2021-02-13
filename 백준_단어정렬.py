from sys import stdin

n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(stdin.readline()[:-1])  # 개행문자 제거
lst = list(set(lst))                   # 같은단어가 입력된 경우, 한번씩만 출력하기 위함

ans = sorted(lst, key = lambda x: (len(x), x))  # 길이가 짧은것 순으로 정렬하되, 길이가 같으면 사전순으로 정렬
for i in ans:
    print(i)