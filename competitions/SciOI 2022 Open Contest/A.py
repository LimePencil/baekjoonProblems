n=int(input())
arr=list(map(int,input().split()))

ways=0
s=dict()
m=1000000007
prev=0
for i in range(n):
    if i==0:
        ways+=1
        prev=1
        s[arr[i]]=1
    else:
        if arr[i] in s:
            ways+=prev
            ways%=m
        else:
            prev=ways+1
            ways+=prev
            prev%=m
            ways%=m
            s[arr[i]]=1
print(ways)