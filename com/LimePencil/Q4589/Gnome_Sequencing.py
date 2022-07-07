import sys

input = sys.stdin.readline
print("Gnomes:")
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    if arr==sorted(arr) or arr==sorted(arr,reverse=True):
        print("Ordered")
    else:
        print("Unordered")