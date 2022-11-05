import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=""
for _ in range(n):
    s+=input()
l=0
r=n-1
ans=""
while l<=r:
    if s[l]<s[r]:
        ans+=s[l]
        l+=1
    elif s[l]>s[r]:
        ans+=s[r]
        r-=1
    else:
        t_l=l+1
        t_r=r-1
        choose_front=True
        while t_l<=t_r:
            if s[t_l]<s[t_r]:
                choose_front=True
                break
            elif s[t_l]>s[t_r]:
                choose_front=False
                break
            else:
                t_l+=1
                t_r-=1
        if choose_front:
            ans+=s[l]
            l+=1
        else:
            ans+=s[r]
            r-=1
print(*[ans[i:i+80] for i in range(0,n,80) ],sep="\n")