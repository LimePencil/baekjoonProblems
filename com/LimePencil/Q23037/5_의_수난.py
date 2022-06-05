import sys

input = sys.stdin.readline
arr = list(map(int,list(input().rstrip())))
s=0
for a in arr:
    s+=a**5
print(s)