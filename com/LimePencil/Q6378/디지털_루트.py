import sys

input = sys.stdin.readline
while True:
    n = list(map(int,list(input().rstrip())))
    if n==[0]:
        break
    while sum(n)>=10:
        n=list(map(int,list(str(sum(n)))))
    print(sum(n))