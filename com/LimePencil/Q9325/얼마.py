import sys

input = sys.stdin.readline
for _ in range(int(input())):
    price=int(input())
    for _ in range(int(input())):
        q,p=list(map(int,input().split()))
        price+=p*q
    print(price)