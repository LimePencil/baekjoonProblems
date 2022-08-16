import sys

input = sys.stdin.readline
b,c = list(map(int,input().split()))
first=int(-b-(b**2-c)**0.5)
second=int(-b+(b**2-c)**0.5)
if first==second:
    print(first)
else:
    print(first,second)