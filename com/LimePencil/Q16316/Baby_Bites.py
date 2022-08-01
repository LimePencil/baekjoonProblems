import sys

input = sys.stdin.readline
n = int(input())
arr = input().split()
weird=False
for i in range(1,n+1):
    if arr[i-1]==str(i) or arr[i-1]=="mumble":
        pass
    else:
        weird=True
        break
print("something is fishy" if weird else "makes sense")