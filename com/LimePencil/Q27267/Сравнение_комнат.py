import sys

input = lambda: sys.stdin.readline().rstrip()
A,B,C,D = list(map(int,input().split()))
print("M" if A*B > C*D else "E" if A*B == C*D else "P")