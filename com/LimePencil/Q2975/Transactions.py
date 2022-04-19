import sys

input = sys.stdin.readline
while True:
    a,b,c=input().split()
    a=int(a)
    c=int(c)
    if a==0 and c==0:
        break
    if b=="W":
        if a-c>=-200:
            print(a-c)
        else:
            print("Not allowed")
    else:
        print(c+a)