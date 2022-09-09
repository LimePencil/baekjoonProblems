import sys

input = sys.stdin.readline
cnt=int(input())
init=int(input())
while True:
    try:
        n=int(input())
        if n%init==0:
            print(n)
            init=int(input())
    except:
        break