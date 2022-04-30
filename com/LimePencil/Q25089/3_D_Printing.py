import sys

input = sys.stdin.readline
n = int(input())
for t in range(1,n+1):
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    p3 = list(map(int,input().split()))
    l = [min(p1[0],p2[0],p3[0]),min(p1[1],p2[1],p3[1]),min(p1[2],p2[2],p3[2]),min(p1[3],p2[3],p3[3])]
    if sum(l)<1000000:
        print("Case #{}: IMPOSSIBLE".format(t))
    else:
        remaining = 1000000
        ls = [0]*4
        for i in range(4):
            if l[i]<=remaining:
                ls[i] = l[i]
                remaining-=l[i]
            else:
                ls[i] = remaining
                remaining = 0
        print("Case #{}: {} {} {} {}".format(t,ls[0],ls[1],ls[2],ls[3]))