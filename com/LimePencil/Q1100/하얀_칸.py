import sys

input = sys.stdin.readline
ans=0
for i in range(8):
    arr=list(input())
    for j in range(8):
        if arr[j]=="F":
            if (i+j)%2==0:
                ans+=1
print(ans)