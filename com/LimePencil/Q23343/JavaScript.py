import sys

input = sys.stdin.readline
a,b = input().split()
if a.isdigit() and b.isdigit():
    print(int(a)-int(b))
else:
    print("NaN")