import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
ans=0
added=0
for i in range(b+1):
    added+=a-2
    ans+=added
print(ans)