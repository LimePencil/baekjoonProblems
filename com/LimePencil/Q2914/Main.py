import sys
import math

a, i = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(a*(i-1)+1)