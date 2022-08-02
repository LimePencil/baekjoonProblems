import sys
from decimal import Decimal

input = sys.stdin.readline
a,b,c = list(map(int,input().split()))
a=Decimal(a)
b=Decimal(b)
c=Decimal(c)
print(a*b/c)