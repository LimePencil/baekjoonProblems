import sys

input = sys.stdin.readline
while True:
    try:
        a,b=list(map(int,input().split()))
        print((b//int(a+1)))
    except:
        break