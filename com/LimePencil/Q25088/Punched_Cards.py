import sys

input = sys.stdin.readline
n = int(input())
for t in range(1,n+1):
    x,y = map(int,input().split())
    print("Case #{}:".format(t))
    hor1 = "+-"*y+"+"
    hor2 = "|."*y+"|"
    print(".."+"+-"*(y-1)+"+")
    print(".."+"|."*(y-1)+"|")
    for _ in range(x-1):
        print(hor1)
        print(hor2)
    print(hor1)