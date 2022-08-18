import math
import sys

input = sys.stdin.read
arr = list(map(int,input().split()))
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
        print(n,"PERFECT")
    elif result<n:
        print(n,"DEFICIENT")
    else:
        print(n,"ABUNDANT")