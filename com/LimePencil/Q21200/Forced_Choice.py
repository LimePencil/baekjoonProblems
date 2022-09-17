import sys

input = lambda: sys.stdin.readline().rstrip()
_,p,s = list(map(int,input().split()))
for _ in range(s):
    a=list(map(int,input().split()))[1:]
    if p in a:
        print("KEEP")
    else:
        print("REMOVE")