import sys
import math
import itertools
n = int(sys.stdin.readline().rstrip("\n"))
m = int(sys.stdin.readline().rstrip("\n"))
if m == 0:
    broken = set()
else:
    broken = set(sys.stdin.readline().rstrip("\n").split(" "))
ans = abs(100 - n)
for i in range(1000001):
    can = True
    for c in str(i):
        if c in broken:
            can = False
            break
    if can:
        if i != 0:
            ans = min(ans, int(math.log10(i))+1+abs(n-i))
        else:
            ans = min(ans, len(str(i))+abs(n-i))
print(ans)

