import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    gone=b*2-a
    print(gone,b-gone)