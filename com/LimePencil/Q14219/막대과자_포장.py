import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
print("YES" if (a*b)%3 == 0 else "NO")