import math
import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(int(input()))]
for n in arr:
    if n==0:
        break
    if n==1:
        print(n,"DEFICIENT")
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
        print(n,"is a perfect number.")
    elif result<n:
        print(n,"is a deficient number.")
    else:
        print(n,"is an abundant number.")
    print()