import sys

input = sys.stdin.readline
a_w=0
b_w=0
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    if a>b:
        a_w+=1
    elif a<b:
        b_w+=1
print(a_w,b_w)