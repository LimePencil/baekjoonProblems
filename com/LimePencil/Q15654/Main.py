import sys
from itertools import permutations

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
c = list(permutations(arr,m,))
for a in c:
    print(*a)
