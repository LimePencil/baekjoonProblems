import sys

input = sys.stdin.readline
n = int(input())
arr = map(int,input().split())
first=True
prev=0
a=0
for i in arr:
    if first==True:
        prev=i
        first=False
    else:
        if prev<i:
            prev=i
        else:
            a=max(a,prev-i)
print(a)