from sys import stdin
from collections import defaultdict
N,M,k = list(map(int, stdin.readline().split()))


lst=[]  # 격자
for _ in range(N):
    lst.append(list(map(int, stdin.readline().split())))  # 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸

tmp=defaultdict(list)
for i in range(N):
    for j in range(N):
        if lst[i][j] == 0:
            continue
        tmp[lst[i][j]] += [(i, j)]  # 번호 :  (x, y) 위치 (0~ N-1)
        lst[i][j]=(lst[i][j],k)


direction = [(-1,0), (1,0), (0,-1), (0,1)]  # 위, 아래, 왼, 우

shark_nowd = defaultdict(list)

sharks=list(map(int, stdin.readline().split()))  # 각 상어의 방향이 주어짐

for i in range(1,len(sharks)+1):
    tmp[i].extend([sharks[i-1]-1])

shark_d=defaultdict(list)
for i in range(1, M+1):
    for j in range(4):

        a = list(map(int,stdin.readline().split()))
        sub = [x-1 for x in a]
        shark_d[i].append(sub)


#print('shark_d : ', shark_d)  # 상어번호 : [(x, y), 방향]

shark=defaultdict(list)
for key, v in tmp.items():
    shark[v[0]]+=[(key,v[1],k)]   # (x,y) : [(상어번호, 방향, 향수크기(k)]

# print(shark)
# print()
# print('-------------------------------------------------------------------------------')
# print()
sec=1
while(sec <= 1000):


    new_shark=[]
    #print('이동시킬 상어 : ', shark)
    # 상어를 이동시킴 (인접한 칸에 아무 냄새 칸이 없으면 원래 자기 자리로 돌아가는 것 계산)
    for key, value in shark.items():
        x, y = key[0], key[1]
        num, d, scent = value[0]
        #print('x, y, num, d, scent: ', x, y, num, d, scent)
        flag=True
        flag_d = []    # 인접한 칸에 자신의 향기가 여러개 일 때를 고려 -> 가장 첫번째로 들어간 것이 최우선
        binkan = []
        for dr in range(len(direction)):
            #print('num, d, dr : ',num,d,dr)
            nx = x + direction[dr][0]
            ny = y + direction[dr][1]
            #print(x, y ,'->', nx, ny)
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if lst[nx][ny]==0:   # 빈칸의 방향을 담는다
                binkan.append(dr)

            else:
                if lst[nx][ny][0] == num:   # 빈칸이 아니면서, 자기자신이 지나온 칸일 경우,
                    flag_d.append(dr)

        #print('상어번호, 빈칸인 칸 : ', num, binkan)
        #print('빈칸이 아니면서, 번호가 자기자신인 칸 : ', num, flag_d)
        if len(binkan) > 1:
            for dr in shark_d[num][d]:
                #print('dr : ', dr)
                if dr in binkan:
                    nx = x + direction[dr][0]
                    ny = y + direction[dr][1]
                    #lst[nx][ny] = (num, scent)
                    new_shark.append([nx, ny, num, dr, scent])
                    flag = False
                    break


        if len(binkan) == 1:
            dr=binkan.pop(0)
            nx = x + direction[dr][0]
            ny = y + direction[dr][1]
            #lst[nx][ny] = (num, scent)
            new_shark.append([nx, ny, num, dr, scent])
            flag = False


        if flag:   # 인접한 곳이 모두 냄새값이 있는 칸일 경우, 자신의 냄새가 들어있는 칸으로 이동
                   # 그런데, 인접한 곳에 자신의 냄새가 있는 칸이 여러개일 경우, 우선순위에 따름
            for dr in shark_d[num][d]:
                if dr in flag_d:
                    nx = x + direction[dr][0]
                    ny = y + direction[dr][1]
                    new_shark.append([nx, ny, num, dr, scent])
                    break

    shark=defaultdict(list)
    for i, j, n, d, sc in new_shark:
        shark[(i, j)] += [(n, d, sc)]


    #print('정렬전 : shark : ', shark)
    # 같은 상어가 있는지 확인 (shark사전 확인)  # 같은 상어가 있으면 -> 상어 번호 순으로 정렬해서 가장 작은 것만 살아남음
    for key,value in shark.items():
        if len(value)>=2:
            value.sort(key = lambda x: x[0])
            shark[key] = [value[0]]

    #print('정렬후 shark : ', shark)

    # 기존의 자리들의 향수크기-1
    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0:
                num, scent = lst[i][j]
                if scent - 1 == 0:
                    lst[i][j] = 0
                else:
                    lst[i][j] = (num, scent - 1)

    #print('상어가 이동되기전 격자 : ', lst)

    # 이동된 상어를 격자에 표시
    for key, value in shark.items():
        #print('key : ', key, ' value : ',value)
        x, y = key[0], key[1]
        n, dre, sc = value[0]
        lst[x][y] = (n, sc)

    #print('이동후 격자 : ', lst)
    # 1번 상어만 격자에 남는지 확인
    cnt_1 = 0
    cnt_el = 0
    for key, value in shark.items():
        if value[0][0] == 1:
            cnt_1 += 1
        else:
            cnt_el += 1

    #print('1번상어 : ', cnt_1, '나머지 상어 : ', cnt_el)
    #print()
    if cnt_1 == 1 and cnt_el == 0:
        break
    sec+=1

if sec > 1000:
    print(-1)
else:
    print(sec)




















