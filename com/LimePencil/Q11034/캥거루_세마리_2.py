import sys

input = sys.stdin.readline
while True:
    try:
        a,b,c=list(map(int,input().split()))
        print(max(c-b,b-a)-1)
    except:
        break