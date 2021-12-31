import sys
from itertools import combinations

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
c = list(combinations(arr,m))
c.sort()
prev = 0
for a in c:
    if prev != a:
        print(*a)
        prev = a