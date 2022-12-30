import math
import sys

input = lambda: sys.stdin.readline().rstrip()

def is_prime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def backtracking(s,k):
    if k==n:
        print(s)
    else:
        for j in [1,3,5,7,9]:
            if is_prime(s*10+j):
                backtracking(s*10+j,k+1)

n = int(input())
for i in [2,3,5,7]:
    backtracking(i,1)