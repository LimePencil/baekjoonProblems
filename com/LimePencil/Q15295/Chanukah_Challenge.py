import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,d= list(map(int,input().split()))
    print(n,(d+1)*d//2+d)