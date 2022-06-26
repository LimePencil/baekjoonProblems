import sys

input = sys.stdin.readline
arr = sorted(list(map(int,input().split())))
s=input().rstrip()
ans=[]
for i in s:
    if i=="A":
        ans.append(arr[0])
    if i=="B":
        ans.append(arr[1])
    if i=="C":
        ans.append(arr[2])
print(*ans)