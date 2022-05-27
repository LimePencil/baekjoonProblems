import sys

input = sys.stdin.readline
for _ in range(int(input())):
    l,w = list(map(int,input().split()))
    if l<12 or w<4:
        print(-1)
    else:
        print(11*w+4)