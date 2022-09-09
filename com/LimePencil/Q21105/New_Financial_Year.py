import sys

input = sys.stdin.readline
for _ in range(int(input())):
    p,c=list(map(float,input().split()))
    print(p/(c/100+1))