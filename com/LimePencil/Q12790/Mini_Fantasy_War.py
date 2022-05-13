import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,e,f,g,h,i=list(map(int,input().split()))
    a+=f
    b+=g
    c+=h
    e+=i
    a=max(a,1)
    b=max(b,1)
    c=max(c,0)
    print(1*a+5*b+2*c+2*e)