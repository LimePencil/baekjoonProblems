import math
import sys

input = sys.stdin.readline
int(input())
arr = list(map(int,input().split()))
for n in arr:
    if n==1:
        print("Deficient")
        continue
    result = 1
    i = 2
    while i<= math.sqrt(n) :
        if n % i == 0 :
            if i == (n / i) :
                result+=i
            else :
                result+=i + n/i
        i+=1
    if result==n:
        print("Perfect")
    elif result<n:
        print("Deficient")
    else:
        print("Abundant")