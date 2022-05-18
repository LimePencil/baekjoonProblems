import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    print("You get {} piece(s) and your dad gets {} piece(s).".format(a//b,a%b))