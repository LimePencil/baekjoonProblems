import math
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    print(int(float.is_integer(math.log2(int(input())))))