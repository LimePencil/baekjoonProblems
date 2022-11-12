import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    a,b,c,d=list(map(int,input().split()))
    e=a*b
    t=c*d
    print("Eurecom" if e<t else "TelecomParisTech" if t<e else "Tie")
