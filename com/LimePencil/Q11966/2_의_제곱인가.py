from math import log2
import sys

input = sys.stdin.readline
n = int(input())
print(int(log2(n).is_integer()))