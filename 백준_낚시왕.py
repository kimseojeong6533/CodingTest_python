from sys import stdin
import copy

R, C, M = list(map(int,stdin.readline().split()))
lst=[]
for _ in range(M):
    lst.append(list(map(int,stdin.readline().split())))  # 위치(x,y), 속력, 이동방향, 크기

for i in lst:
    i[0]=i[0]-1
    i[1]=i[1]-1


zido=[[0]*C for _ in range(R)]
for i in lst:
    zido[i[0]][i[1]]=[i[2],i[3],i[4]]

person=0
fishing=0
# print('초기지도 : ',zido)
# print()


while(person<C):
    print('사람위치 : ',person,'fishing : ',fishing)

    # 낚시꾼이 위치한 열에서 가장 가까운 상어를 잡는다
    sub=[]
    for i in lst:
        x,y,s,d,size=i
        if y == person:
            sub.append([x,y,s,d,size])

    sub.sort(key=lambda x:x[0])
    #print(sub)
    if sub !=[]:
        fished_shark = sub.pop(0)  # 가장 가까운 상어를 잡았다
        zido[fished_shark[0]][fished_shark[1]]=0  # 잡은 위치에 0을 넣음
        fishing += fished_shark[4]

    # 잡은 상어를 제외한 배열을 만들어야함
    lst_copy=[i for i in lst if i != fished_shark]
    print('lst_copy : ',lst_copy)
    # 상어의 이동
    lst=[]
    for i in lst_copy:
        x,y,s,d,size= i   # d : 1 -위, 2 - 아래, 3- 오른, 4- 왼쪽
        new_x, new_y, new_d, new_s = x, y, d, s
        zido[x][y]=0

        moving=0
        # 1씩 까면서, 방향전환
        while moving<s:
            if size==9:
                print('x,y,new_x,new_y : ', x, new_x, y, new_y)
                print()
            if new_d == 1:  # 위
                new_x=new_x-1
                if new_x < 0:
                    new_x = abs(new_x)
                    new_d=2

            elif new_d == 2:  # 아래
                new_x=new_x+1
                if new_x>=R:
                    new_x-=1
                    new_d=1

            elif new_d == 3:  # 오른
                new_y=new_y+1
                if new_y>=C:
                    new_y-=1
                    new_d=4

            elif new_d==4:
                new_y=new_y-1
                if new_y<0:
                    new_y=abs(new_y)
                    new_d=3

            moving+=1


        if zido[new_x][new_y] == 0: # 새로운 위치에 상어가 없다면,
            zido[x][y] = 0          # 기존 위치에는 0을 넣고
            zido[new_x][new_y] = [s, new_d, size]  # 새로운 위치에 속도, 방향, 크기를 넣어준다

        elif zido[new_x][new_y]!=0: # 같은 위치에서는 가장 큰 상어만 살아남는다
            #print('같은위치 상어들',new_x,new_y)
            tmp=[zido[new_x][new_y]]
            tmp.append([s,new_d,size])  # 속도 방향 사이즈
            #print('tmp: ',tmp)
            tmp.sort(key=lambda x:(-x[2]))
            #print(tmp)
            # winner=tmp[0]
            zido[new_x][new_y]=[tmp[0]]  # 가장 큰상어만 남음.
            #zido[x][y] = 0

        lst.append([new_x, new_y, s, new_d, size])
        # print()
        # print('zido : ', zido)
        # print()

    print('초기지도 : ', zido)

    person+=1