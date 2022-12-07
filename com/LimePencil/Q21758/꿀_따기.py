import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
s=[arr[0]]*n
for i in range(1,n):
    s[i]=s[i-1]+arr[i]
# location of honey
front=0
for i in range(1,n-1):
    front=max(front,s[i-1]+s[n-2]-arr[i])
    

middle=s[n-2]-s[0]+max(arr[1:n])
back=0
for i in range(n-2,0,-1):
    back=max(back,s[n-1]-s[0]-arr[i]+s[n-1]-s[i])

print(max(front,middle,back))