n=int(input())
ans=0
cnt=0
e=sorted([int(input()) for i in range(n)],reverse=True)
if len(e)>42:
    e=e[:42]
for l in e:
    cnt+=l
    if l>=60:
        ans+=1
    if l>=100:
        ans+=1
    if l>=140:
        ans+=1
    if l>=200:
        ans+=1
    if l>=250:
        ans+=1
print(cnt,ans)