import sys
import math
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a=int(input())
    m = 0
    for i in range(2,a+1):
        temp = a
        while temp!=1:
            if temp%i == 0:
                m +=1
                temp//=i
            else:
                break
    print(m)