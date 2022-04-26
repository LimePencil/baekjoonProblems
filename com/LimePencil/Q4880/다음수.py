import sys

input = sys.stdin.readline
while True:
    a,b,c=list(map(int,input().split()))
    if a==0 and b==0 and c==0:
        break
    if c-b==b-a:
        print("AP",2*c-b)
    elif b//a==c//b:
        print("GP",c**2//b)