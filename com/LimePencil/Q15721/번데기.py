import sys

input = lambda: sys.stdin.readline().rstrip()
a = int(input())
t = int(input())
g = int(input())

if g==0:
    bbun=0
    degi=0
    th=2
    prev_th=0
    for i in range(30000):
        n=i-prev_th
        if n==0 or n==2:
            bbun+=1
        elif n==1 or n==3:
            degi+=1
        elif 4<=n<4+th:
            bbun+=1
        else:
            if n==4+2*th-1:
                th+=1
                prev_th=i+1
            degi+=1
        if bbun==t:
            print(i%a)
            break
else:
    bbun=0
    degi=0
    th=2
    prev_th=0
    for i in range(30000):
        n=i-prev_th
        if n==0 or n==2:
            bbun+=1
        elif n==1 or n==3:
            degi+=1
        elif 4<=n<4+th:
            bbun+=1
        else:
            if n==4+2*th-1:
                th+=1
                prev_th=i+1
            degi+=1
        if degi==t:
            print(i%a)
            break