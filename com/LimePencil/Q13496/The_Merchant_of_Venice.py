import sys

input = sys.stdin.readline

for i in range(1,int(input())+1):
    n,s,d=list(map(int,input().split()))
    furthest=s*d
    ans=0
    for _ in range(n):
        dist,val=map(int,input().split())
        if dist<=furthest:
            ans+=val
    print("Data Set {}:".format(i))
    print(ans)
    print()