import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=input()
ans=''
for i in range(0,len(s),n):
    ans+=s[i]
print(ans)