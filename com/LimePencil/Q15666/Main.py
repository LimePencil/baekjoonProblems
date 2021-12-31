import sys
from itertools import combinations_with_replacement

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
c = list(combinations_with_replacement(arr,m))
c.sort()
prev = 0
for a in c:
    if prev != a:
        print(*a)
        prev = a