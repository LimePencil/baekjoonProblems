import sys

input = sys.stdin.readline
a=0
b=0
for _ in range(int(input())):
    a_card,b_card=map(int,input().split())
    if a_card>b_card:
        a+=a_card+b_card
    elif a_card==b_card:
        a+=a_card
        b+=b_card
    else:
        b+=a_card+b_card
print(a,b)