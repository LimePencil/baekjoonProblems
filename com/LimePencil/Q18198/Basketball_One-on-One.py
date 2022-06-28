import sys

input = sys.stdin.readline
arr = list(input().rstrip())
a=0
b=0
for i in range(0,len(arr),2):
    if "A" == arr[i]:
        a+=int(arr[i+1])
    else:
        b+=int(arr[i+1])
print("A" if a>b else "B")