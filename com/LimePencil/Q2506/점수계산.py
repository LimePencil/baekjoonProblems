n=int(input())
a=list(map(int,input().split()))
prev=0
streak=0
ans=0
for i in a:
    if prev==1 and i==1:
        streak+=1
    elif i==1:
        streak=1
    else:
        streak=0
    ans+=streak
    prev=i
print(ans)