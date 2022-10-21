import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
print(*sorted(list(Counter(list(input())).items()),key=lambda x:(-x[1],x[0]))[0])