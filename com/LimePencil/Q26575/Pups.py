import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    d,f,p = list(map(float,input().split()))
    print(f"${d*f*p:.2f}")