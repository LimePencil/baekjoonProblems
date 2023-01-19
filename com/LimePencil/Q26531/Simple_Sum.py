import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
print("YES" if eval(s[:5])==int(s[8]) else "NO")