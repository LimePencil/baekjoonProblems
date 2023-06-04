import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
x=0
for e in arr:
    if 4<=e<=15:
        x^=1
    elif 16<=e<=81:
        x^=2
    elif 6724<=e<=50625:
        x^=3
    elif 50626<=e<=2562991875:
        x^=1
    elif e>=2562991876:
        x^=2
print("koosaga" if x else "cubelover")