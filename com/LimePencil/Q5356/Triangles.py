import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    a,b=input().split()
    b=ord(b)-1
    a=int(a)
    for i in range(1,a+1):
        print(chr((b+i-65)%26+65)*i)
    print()
