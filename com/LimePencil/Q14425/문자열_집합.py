from collections import Counter
import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
d=Counter([input().rstrip() for _ in range(n)])
print(sum([int(input().rstrip() in d) for _ in range(m)]))