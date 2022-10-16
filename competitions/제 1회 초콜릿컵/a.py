import sys

input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())):
    w=0
    b=0
    r,c=sorted(list(map(int,input().split())))
    b=(2*r**3-2*r)//3+(c-r)*r**2
    w=b+r
    print(w,b)