import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = list(map(int,input().split()))
x=0
for e in p:
    if e%4==3:
        x^=e+1
    elif e%4==0:
        x^=e+-1
    else:
        x^=e
if x!=0:
    print("koosaga")
else:
    print("cubelover")