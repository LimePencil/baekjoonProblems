import sys
from itertools import combinations

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
c = list(combinations(arr,m))
for a in c:
    print(*a)