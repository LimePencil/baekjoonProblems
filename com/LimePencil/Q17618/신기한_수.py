import sys

input = sys.stdin.readline
n = int(input())
cnt=0
for i in range(1,n+1):
    s=0
    j=i
    while j>0:
        s+=j%10
        j//=10
    if i%s==0:
        cnt+=1
print(cnt)