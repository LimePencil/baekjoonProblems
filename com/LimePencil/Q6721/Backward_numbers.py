import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,b = list(map(int,input()[::-1].split()))
    ans = a+b
    print(int(str(ans)[::-1]))