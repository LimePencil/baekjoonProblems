n=int(input())
m=list(map(int,input().split()))
ans=[]
for e in m:
    if e==300:
        ans.append(1)
    elif e>=275:
        ans.append(2)
    elif e>=250:
        ans.append(3)
    else:
        ans.append(4)
print(*ans)