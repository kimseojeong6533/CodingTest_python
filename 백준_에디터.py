from sys import stdin
inst = list(stdin.readline())[:-1]

M = int(stdin.readline()[:-1])

lst = []
for _ in range(M):
    lst.append(stdin.readline()[:-1])


# 처음 답 : 시간초과

# cursor = len(inst)
# for i in lst:
#     if i[0] == "L":
#         if cursor == 0:
#             continue
#         cursor -= 1   # 커서를 왼쪽으로 한칸 옮김
#
#     elif i[0] == 'D':
#         if cursor == len(inst):
#             continue
#         cursor += 1
#
#     elif i[0] == 'B':
#         if cursor == 0:
#             continue
#         inst = inst[:cursor-1] + inst[cursor:]
#         cursor -= 1
#
#     else:  # P
#         add_c = i[2]
#         inst = inst[:cursor]+add_c+inst[cursor:]
#         cursor += 1
#
# print(inst)

# 두번째 답 :

# 커서를 기준으로 왼쪽에 있는 문자열 리스트(inst), 오른쪽에 있는 문자열리스트(right)로 나눠서 나중에 둘을 통합하여 출력


right = []
print("lst : ",lst)
for i in lst:

    if i[0] == 'L':
        if inst:
            right.append(inst.pop(-1))

    elif i[0] == 'D':
        if right:
            inst.append(right.pop(-1))
    elif i[0] == 'B':
        if inst:
            inst.pop(-1)
    elif i[0] == 'P':   # P일 때
        inst.append(i[2])



print(''.join(inst+right[::-1]))



