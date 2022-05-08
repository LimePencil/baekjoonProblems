from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
d=Counter(list(map(int,input().split())))
m=int(input())
q = list(map(int,input().split()))
print(*[int(q[i] in d) for i in range(m)])