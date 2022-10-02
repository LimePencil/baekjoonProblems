import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

s=n*4-3
arr=[[" "]*s for _ in range(s)]
for i in range(1,n+1):
    start=2*i-2
    end=s-(2*i-2)-1

    for k in range(start,end+1):
        for l in range(start,end+1):
            if k==start or k==end or l==start or l==end:
                arr[k][l]="*"

for i in range(s):
    print("".join(arr[i]))
