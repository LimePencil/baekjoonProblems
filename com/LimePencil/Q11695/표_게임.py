import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
table=[sum(map(int,input().split())) for _ in range(n)]

x=0
for e in table:
    x^=e
if x!=0:
    print("august14")
else:
    print("ainta")