import sys

input = sys.stdin.readline

n = int(input())
x,y=list(map(int,input().split()))
for _ in range(n-1):
    dir,mag =input().split()
    mag=int(mag)
    if dir =="N":
        y+=mag
    elif dir=="S":
        y-=mag
    elif dir=="E":
        x+=mag
    elif dir=="W":
        x-=mag
    elif dir =="NE":
        x+=mag*2**0.5/2
        y+=mag*2**0.5/2
    elif dir=="SE":
        x+=mag*2**0.5/2
        y-=mag*2**0.5/2
    elif dir=="SW":
        x-=mag*2**0.5/2
        y-=mag*2**0.5/2
    elif dir=="NW":
        x-=mag*2**0.5/2
        y+=mag*2**0.5/2
print(x,y)