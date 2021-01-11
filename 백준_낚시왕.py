from sys import stdin
import copy   # copy.deepcopy 지양하자 써야만 하는 경우에는 그냥 =처리

R, C, M = list(map(int,stdin.readline().split()))

# 상어 정보
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


while (person<C):
    sub=[]
    for i in lst:
        x,y,s,d,size=i
        if y == person:
            sub.append([x,y,s,d,size])
    sub.sort(key=lambda x:x[0])

    if len(sub)>0:
        fished_shark=sub.pop(0)
        #print('fished_shark : ',fished_shark)
        zido[fished_shark[0]][fished_shark[1]]=0
        fishing+=fished_shark[4]
        lst=[i for i in lst if i != fished_shark]


    # 상어를 움직임
    next_sharks = []
    for i in lst:
        x, y, s, d, size = i                     # 현재 상어위치 및 속도, 방향
        new_x, new_y, new_d, new_s = x, y, d, s  # 다음 상어위치 및 속도, 방향,
        zido[x][y] = 0

        moving=0
        while(moving<s):

            if new_d == 1:  # 위
                new_x = new_x - 1
                if new_x < 0:
                    new_x = abs(new_x)
                    new_d = 2

            elif new_d == 2:  # 아래
                new_x = new_x + 1
                if new_x >= R:
                    new_x -= 2
                    new_d = 1

            elif new_d == 3:  # 오른
                new_y = new_y + 1
                if new_y >= C:
                    new_y -= 2
                    new_d = 4

            elif new_d == 4:
                new_y = new_y - 1
                if new_y < 0:
                    new_y = abs(new_y)
                    new_d = 3

            moving+=1

        next_sharks.append([new_x,new_y,s,new_d,size])

    for i in next_sharks:
        x,y,s,d,size=i

        if zido[x][y]==0:
            zido[x][y]=[[s,d,size]]

        else:
            zido[x][y].append([s,d,size])


    for i in range(R):
        for j in range(C):
            if (zido[i][j])!=0 and len(zido[i][j])>1:
                survived=sorted(zido[i][j],key=lambda x:x[2])[-1]
                zido[i][j]=[survived]

    lst = []
    for i in range(R):
        for j in range(C):
            if zido[i][j]!=0:
                v=[i,j]+zido[i][j][0]
                lst.append(v)


    person+=1

print(fishing)