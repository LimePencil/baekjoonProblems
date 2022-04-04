import sys

input = sys.stdin.readline
n,m = map(int,input().split())
found = False
idx = 0
for i in range(2,m):
    if n%i ==0:
        found = True
        idx = i
        break
print("BAD {}".format(idx) if found else "GOOD")