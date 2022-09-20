import sys

input = lambda: sys.stdin.readline().rstrip()
n,m=map(int,input().split())
arr = [input() for _ in range(n)]
s=sum([len(a) for a in arr])
under=m-s
per_word=under//(n-1)
use_one_more=under-per_word*(n-1)
ans=arr[0]
for i in range(1,n):
    ans+="_"*per_word
    if arr[i][0].islower() and use_one_more>0:
        ans+="_"
        use_one_more-=1
    elif i +use_one_more==n and  use_one_more>0 :
        ans+="_"
        use_one_more-=1
    ans+=arr[i]
print(ans)