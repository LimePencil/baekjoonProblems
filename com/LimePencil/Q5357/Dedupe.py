import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    s=input()
    ans=s[0]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            ans+=s[i]
    print(ans)