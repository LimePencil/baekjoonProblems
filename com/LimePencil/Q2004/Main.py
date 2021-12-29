import sys
import math

def two(num):
    count = 0 
    while(num >= 2):
        count += num//2
        num //= 2
    return count
def five(num):
    count = 0 
    while(num >= 5):
        count += num//5
        num //= 5
    return count

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
a = two(n)-two(n-k)-two(k)
b = five(n)-five(n-k)-five(k)

print(min(a,b))