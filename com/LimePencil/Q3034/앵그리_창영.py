import sys

input = sys.stdin.readline
n,w,h = list(map(int,input().split()))
poss=(w**2+h**2)**0.5
for _ in range(n):
    a=int(input())
    print("DA" if a<=poss else "NE")