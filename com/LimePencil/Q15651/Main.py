import sys
from itertools import product

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))

ls = list(product(range(1,n+1),repeat=m))
ans = ""
for x in ls:
    ans += " ".join(list(map(str,x))) + "\n"
sys.stdout.write(ans)