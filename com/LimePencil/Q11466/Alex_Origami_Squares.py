import sys

input = sys.stdin.readline
a,b = sorted(list(map(int,input().split())))
candidates=[]
if b<=3*a:
    candidates.append(b/3)
else:
    candidates.append(a)
candidates.append(a/2)

print(max(candidates))