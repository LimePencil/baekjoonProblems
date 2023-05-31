import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = list(map(int,input().split()))
x=0
for e in p:
    x^=e
if x!=0:
    print("koosaga")
else:
    print("cubelover")