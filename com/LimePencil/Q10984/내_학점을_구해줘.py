import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s=0
    avg=0
    for i in range(int(input())):
        a,b = input().split()
        a=int(a)
        b=float(b)
        s+=a
        avg+=b*a
    avg/=s

    print(s,avg)