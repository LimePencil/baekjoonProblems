import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c=list(map(float,input().split()))
    d,e,f=list(map(float,input().split()))
    first=0
    second=0
    first+=a*e
    first+=b*f
    first+=c*d
    second+=b*d
    second+=e*c
    second+=f*a
    print("ADAM" if first>second else ("=" if first == second else "GOSIA"))