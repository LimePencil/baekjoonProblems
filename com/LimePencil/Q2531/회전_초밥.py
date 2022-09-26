import sys

input = lambda: sys.stdin.readline().rstrip()
n,d,k,c = list(map(int,input().split()))
sushi=[int(input()) for _ in range(n)]
ans=0
for i in range(n):
    s=i
    e=(i+k-1)%n
    st=None
    if s<e:
        st=set(sushi[s:e+1])
    else:
        st=set(sushi[:e+1] +sushi[s:])
    st.add(c)
    ans=max(ans,len(st))
print(ans)