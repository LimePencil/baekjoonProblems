n,m,k=map(int,input().split())
ans=0
while n>1 and m>0 and n+m-3>=k:
    n-=2
    m-=1
    ans+=1
print(ans)