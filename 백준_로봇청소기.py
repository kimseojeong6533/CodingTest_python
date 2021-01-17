from sys import stdin

direction=[(-1,0), (0,1),(1,0),(0,-1)]  # 북, 동, 남, 서

N, M =list(map(int,stdin.readline().split()))
i, j, d =list(map(int,stdin.readline().split()))


lst=[]
for _ in range(N):
    lst.append(list(map(int,stdin.readline().split())))

cleaned=0  # 로봇청소기가 청소하는 칸의 캐수

while(1):

    # 현재위치를 청소한다
    if lst[i][j]==0:
        lst[i][j]=9
        cleaned+=1

    # 현재위치에서 현재방향을 기준으로 왼쪽부터 차례대로 탐색 (벽인지, 빈칸이면서 청소되어 있지 않은 공간인지)
    searching=d-1
    if searching<0:
        searching=3
    cnt=0
    flag=False
    x, y = 0, 0
    while(cnt<4):
        x=i+direction[searching][0]
        y=j+direction[searching][1]

        if lst[x][y]==1 or lst[x][y]==9: # 벽을만나거나 청소한 칸을 만나면
            searching-=1
            if searching < 0:
                searching = 3
            cnt += 1

        elif lst[x][y]==0: # 청소하지않은 칸을 만나면
            flag=True
            break

    if flag:  # 왼쪽방향에 아직 청소하지않은 빈칸이 있다면
        i, j = x, y
        d = searching


    else:  #4방이 모두 벽이거나 청소했다면

        # 뒷쪽 위치
        i = i - direction[d][0]
        j = j - direction[d][1]
        if lst[i][j]==1: #네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
            break

print(cleaned)



