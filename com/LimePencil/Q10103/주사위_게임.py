import sys

input = sys.stdin.readline
a=100
b=100
for _ in range(int(input())):
    a_num,b_num=list(map(int,input().split()))
    if a_num > b_num:
        b-=a_num
    elif a_num<b_num:
        a-=b_num
print(a)
print(b)