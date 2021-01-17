from sys import stdin

N,M,K = list(map(int,stdin.readline().split()))

fireball=[]
for _ in range(M):
    fireball.append(list(map(int,stdin.readline().split()))) # 행, 열, 질량, 속력, 방향


lst=[[0]*N for _ in range(N)]

sub=[]
while fireball:
    i,j,m,s,d = fireball.pop()
    lst[i-1][j-1]=[[i-1,j-1,m,s,d]]  # 초기파이어볼 표시
    sub+=[[i-1,j-1,m,s,d]]      # 위치인덱스를 다르게 했기 때문에 따로 처리

# fireball.extend(sub)
fireball=sub
#print(fireball)
# # #             0      1   2       3     4    5       6       7
direction=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

cnt=1
#파이어볼에게 K번 이동을 명령
while(cnt<=K):

    #모든 파이어볼이 방향과 속력만큼 이동
    new_fireball=[]
    while fireball:
        i, j, m, s, d = fireball.pop()
        lst[i][j]=0
        next_x, next_y = i, j             # 속력만큼 이동하기위해, 초기화선언을 해줌

        mov=0
        while(mov<s):  # 자신의 방향과 속력만큼 이동
            next_x = next_x + direction[d][0]
            next_y = next_y + direction[d][1]
            mov+=1

        next_x=next_x%N
        next_y=next_y%N
        # while(1):
        #     if next_x>=0 and next_x<N and next_y>=0 and next_y<N:
        #         break
        #     if next_x>=N:
        #         next_x=next_x-N
        #     if next_x<0:
        #         next_x=next_x+N
        #     if next_y>=N:
        #         next_y=next_y-N
        #     if next_y<0:
        #         next_y=next_y+N
        new_fireball+=[[next_x,next_y,m,s,d]]


    fireball = new_fireball


    # 격자에 이동한 파이어볼 표시
    for i,j,m,s,d in fireball:
        if lst[i][j]==0:
            lst[i][j]=[[i,j,m,s,d]]
        else:
            lst[i][j]+=[[i,j,m,s,d]]

    remov_fireball=[]


    for i in range(N):
        for j in range(N):
            if lst[i][j]==0:
                continue

            if (lst[i][j])!=0 and len(lst[i][j])>=2:   # 2개 이상의 파이어볼이 있는 칸에서는

                new_m, new_s, new_d_jjak, new_d_hol, new_d = 0, 0, 0, 0, []

                for lst_elem in lst[i][j]:
                    x, y, m, s, d = lst_elem[0], lst_elem[1], lst_elem[2], lst_elem[3], lst_elem[4]
                    remov_fireball.append([x, y, m, s, d])
                    new_m+=m
                    new_s+=s
                    if d%2==0:
                        new_d_jjak+=1
                    else:
                        new_d_hol+=1

                if new_m<5:
                    lst[x][y] = 0  # 질량이 0인 파이어볼은 소멸됨.

                    continue

                new_m = new_m//5
                new_s = (new_s)//(len(lst[i][j]))


                if new_d_jjak==len(lst[i][j]) or new_d_hol==len(lst[i][j]):
                    new_d=[0,2,4,6]
                else:
                    new_d=[1,3,5,7]

                for fly_d in new_d:
                    fireball+=[[i,j,new_m,new_s,fly_d]]




    fireball = [x for x in fireball if x not in remov_fireball]
    cnt+=1

total_m=0
for i,j,m,s,d in fireball:
    total_m+=m

print(total_m)






























