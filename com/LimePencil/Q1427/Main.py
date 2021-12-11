import sys

n = sys.stdin.readline()
ls = list(n)
ls.sort(reverse=True)
ans=""
for x in ls:
    ans+=x
sys.stdout.write(ans)