import sys
import math

input = lambda: sys.stdin.readline().rstrip()


 
def find_sum_of(n) :
    s = 0
    i = 1
    for i in range(1, int(n**0.5)+1):
        if n%i == 0 :
            if n//i == i :
                s +=i
            else :
                s +=i
                s +=(n // i )
    s = s - n
    return s
 
def isAbundant(n) :
    if (find_sum_of(n) > n) :
        return True
    else :
        return False
    
for i in range(int(input())):
    n=int(input())
    if isAbundant(n):
        for j in range(1,n):
            if n%j==0 and isAbundant(j):
                print("BOJ 2022")
                break
        else:
            print("Good Bye")
    else:
        print("BOJ 2022")