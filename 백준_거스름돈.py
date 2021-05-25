from sys import stdin


m = int(stdin.readline())
money = 1000-m
d = {x:0 for x in [500,100,50,10,5,1]}

for k,v in d.items():
    a,b = divmod(money,k) # 몫과 나머지를 구하는 함수 (money//k, money%k)리턴
    if a > 0 :
        d[k] = a
        money = b
print(sum(list(d.values())))

