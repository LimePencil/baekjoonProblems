from decimal import ROUND_HALF_UP, Decimal
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    r,g,b=0,0,0
    for _ in range(10):
        x,y,z=list(map(int,input().split()))
        r+=x
        g+=y
        b+=z
    r=Decimal(r)/Decimal(10)
    g=Decimal(g)/Decimal(10)
    b=Decimal(b)/Decimal(10)
    print(r.quantize(Decimal('1.'),rounding=ROUND_HALF_UP),g.quantize(Decimal('1.'),rounding=ROUND_HALF_UP),b.quantize(Decimal('1.'),rounding=ROUND_HALF_UP))
    
