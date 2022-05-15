import sys

input = sys.stdin.readline
n = int(input())
ans=""
while n>0:
    ans+=str(n%9)
    n//=9
print(ans[::-1])