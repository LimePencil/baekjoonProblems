import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()
MOD=998244353
n=int(input())
arr=[]
for i in range(n):
    m,a=map(int,input().split())
    arr.append(a)
s=sum(arr)
ans=0
for i in range(1,s+1):
    c=combinations(arr,i)
    for o in c:
        if i%2==1:
            ans+=s*pow(sum(o),MOD-2,MOD)%MOD
        else:
           ans-=s*pow(sum(o),MOD-2,MOD)%MOD
           ans+=MOD
        ans%=MOD


print(ans)
