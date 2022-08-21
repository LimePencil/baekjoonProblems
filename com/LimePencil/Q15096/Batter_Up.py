import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
s=0
cnt=0
for i in arr:
    if i==-1:
        continue
    else:
        cnt+=1
        s+=i
print(s/cnt)