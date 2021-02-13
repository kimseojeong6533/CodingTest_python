from sys import stdin

board = stdin.readline().split('.')
board2 = [x.strip('\n') for x in board]  # 끝에 개행문자 제거
#print(board2)

lst = []
for i in board2:
    if i=='':
        continue

    if len(i)//4>=1:
        a, b = divmod(len(i), 4)
        if b%2!=0:     # 글자의 수가 4이상이고 나머지값이 2로 나누어 지지 않을 때 즉, AAAA이후, BB로 덮을 수 없을 때
            print(-1)
            break
        else:          # AAAA와 BB로 덮을 수 있기 때문에 4로 나눈 몫만큼 AAAA를, 4로 나눈 나머지를 다시 2로 나눈 몫만큼 BB를 덮어줌
            lst.append('AAAA'*(a)+'BB'*(b//2))

    else:
        if len(i)==2:                 #글자가 4보다 적지만, BB로 덮을 수 있을 때, 즉, 글자의 수가 2일 때
            lst.append('BB')
        else:                         #글자수가 1 또는 3인 경우, 덮을수 없으므로 바로 break
            print(-1)
            break


else:
    answer = ''
    for i in board2:

        if i=='':
            answer+='.'
        else:
            answer+=lst.pop(0)+'.'   # 이런 식으로 하면 끝문자에도 .이 들어가므로 슬라이싱 처리

    print(answer[:-1])







