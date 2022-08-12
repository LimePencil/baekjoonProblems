import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
cnt=2
while a>=b:
    temp=a
    a=b
    b=temp-b
    cnt+=1
print(cnt)