import sys

input = sys.stdin.readline
for _ in range(int(input())):
    ans = 0
    n,m= list(map(int,input().split()))
    for i in range(1,n):
        for j in range(i+1,n):
            if (i**2+j**2+m)%(i*j) ==0:
                ans+=1
    print(ans)