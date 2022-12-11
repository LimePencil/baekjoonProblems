import sys
import re

input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    s = input()
    vega=True
    r=re.compile('(100+1+|01)+')
    vega=r.fullmatch(s)
    print("YES" if vega else "NO")