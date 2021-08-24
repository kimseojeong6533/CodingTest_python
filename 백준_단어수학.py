# from sys import stdin
# from collections import defaultdict
#
# # 그리디 알고리즘 : 각 단계에서 최선의 선택을 한다
#
# d = defaultdict(int)
# N = int(stdin.readline())
# lst = []
# for _ in range(N):
#     lst.append(stdin.readline()[:-1])  # '\n'을 제외해주기 위해서 [:-1] 추가
#
# lst.sort(key = len, reverse=True)
#
# std_len = len(lst[0])
#
# IntLst = []
#
# std_int = 9
# for i in range(-std_len,0):
#     sub_d = []
#
#     for j in lst:
#         if (-i) > len(j):
#             continue
#         j[i].count() > 0
print('1'*4)