import sys

input = sys.stdin.readline
n,s=map(int,input().split())
arr=list(map(int,input().split()))
high=1<<n
count=0
for i in range(1,high):
    poss=("{:0"+str(n)+"b}").format(i)
    add=0
    for j in range(n):
        if poss[j]=="1":
            add+=arr[j]
    if add==s:
        count+=1
print(count)