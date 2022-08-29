import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x,w = list(map(int,input().split()))
    cnt=0
    while x<w:
        x*=2
        cnt+=1
    print(cnt)