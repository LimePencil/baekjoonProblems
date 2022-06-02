import sys

input = sys.stdin.readline
a,b,c = list(map(int,input().split()))
print(a^b if c%2==1 else a)