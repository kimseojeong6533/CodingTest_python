from sys import stdin

T = int(stdin.readline())
lst = []
for _ in range(T):
    lst.append(int(stdin.readline()))

def Fibonacci(i):
    if i == 0:
        d[0] += 1
        return 0

    if i == 1:
        d[1] += 1
        return 1

    return Fibonacci(i - 1) + Fibonacci(i - 2)

for n in lst:
    d = {}
    d[0]=0
    d[1]=0
    Fibonacci(n)
    print(d[0], d[1])

