import sys

def fib1(n):
    global cnt1
    if n==1 or n==2:
        cnt1+=1
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

input = sys.stdin.readline
n = int(input())
cnt1=0
fib1(n)
print(cnt1,n-2)