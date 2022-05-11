import sys

input = sys.stdin.readline
n = int(input())
ans=0
for i in range(1,n+1):
    s=str(i)
    ans+=s.count("3")
    ans+=s.count("6")
    ans+=s.count("9")
print(ans)