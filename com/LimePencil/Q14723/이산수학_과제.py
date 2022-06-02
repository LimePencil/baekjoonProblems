import sys

input = sys.stdin.readline
n = int(input())
a=1
while a*(a+1)//2<n:
    a+=1
last=a*(a-1)//2
after=a*(a+1)//2
a+=1
print(after-n+1,n-last)