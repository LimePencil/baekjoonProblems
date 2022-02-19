import sys
from math import ceil
l = int(sys.stdin.readline().rstrip("\n"))
a = int(sys.stdin.readline().rstrip("\n"))
b = int(sys.stdin.readline().rstrip("\n"))
c = int(sys.stdin.readline().rstrip("\n"))
d = int(sys.stdin.readline().rstrip("\n"))

print(l-max(ceil(a/c),ceil(b/d)))