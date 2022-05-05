import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    m=0
    if a==0:
        pass
    elif a<=1:
        m+=5000000
    elif a<=3:
        m+=3000000
    elif a<=6:
        m+=2000000
    elif a<=10:
        m+=500000
    elif a<=15:
        m+=300000
    elif a<=21:
        m+=100000

    if b==0:
        pass
    elif b<=1:
        m+=5120000
    elif b<=3:
        m+=2560000
    elif b<=7:
        m+=1280000
    elif b<=15:
        m+=640000
    elif b<=31:
        m+=320000

    print(m)