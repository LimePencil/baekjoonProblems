import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
limit=[100,100,200,200,300,300,400,400,500]
for i in range(len(arr)):
    if arr[i]>limit[i]:
        print("hacker")
        break
else:
    if sum(arr)>=100:
        print("draw")
    else:
        print("none")