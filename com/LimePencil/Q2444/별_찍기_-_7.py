n = int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))