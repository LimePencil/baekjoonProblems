import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
ans=0
added=1
for i in range(b+1):
    ans+=added
    added+=a-2
print(ans)