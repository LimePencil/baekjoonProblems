import sys

input = sys.stdin.readline
a1,h1= list(map(int,input().split()))
a2,h2= list(map(int,input().split()))
while h1>0 and h2>0:
    h1-=a2
    h2-=a1
if h1<=0 and h2<=0:
    print("DRAW")
elif h2<=0:
    print("PLAYER A")
else:
    print("PLAYER B")