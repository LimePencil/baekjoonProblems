import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    print("Case {}: {}".format(t,sum(list(map(int,input().split())))))