import sys

input = sys.stdin.readline
n = int(input())
while True:
    s=sum(map(int,str(n)))
    if n%s==0:
        print(n)
        break
    n+=1