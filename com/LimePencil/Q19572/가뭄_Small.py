import sys

input = lambda: sys.stdin.readline().rstrip()
n,m,k = list(map(int,input().split()))
s=(n+m+k)/2
if n<s and m<s and k<s:
    print(1)
    print(f"{s-k:.1f} {s-m:.1f} {s-n:.1f}")
else:
    print(-1)