import sys
from itertools import combinations

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))

ls = list(combinations(range(1,n+1),m))
ans = ""
for x in ls:
    ans += " ".join(list(map(str,x))) + "\n"
sys.stdout.write(ans)