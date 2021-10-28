import sys

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
note = dict()
ans = ""
for i in range(n):
    site, password = sys.stdin.readline().strip('\n').split(" ")
    note[site] = password
for i in range(m):
    site = sys.stdin.readline().strip('\n')
    ans += note[site] + "\n"
sys.stdout.write(ans)