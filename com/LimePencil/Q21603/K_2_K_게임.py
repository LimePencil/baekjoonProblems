import sys

input = sys.stdin.readline
n,k = list(map(int,input().split()))
ans=[]
for i in range(1,n+1):
    if i%10!=k%10 and  i%10!=(2*k)%10:
        ans.append(i)
print(len(ans))
print(*ans)