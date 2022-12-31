import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
ans=[]
for i in range(1,n+1):
    ans.append(str(i))
    if i%6==0:
        ans.append("Go!")
if ans[-1]!="Go!":
    ans.append("Go!")
print(*ans)