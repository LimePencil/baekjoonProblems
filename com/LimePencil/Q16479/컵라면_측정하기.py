import sys

input = sys.stdin.readline
k = int(input())
d1,d2 = list(map(int,input().split()))
print(k**2-((d2-d1)/2)**2)