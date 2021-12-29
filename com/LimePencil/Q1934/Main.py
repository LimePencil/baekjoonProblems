import sys

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    q = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    q.sort()
    A,B =q
    a,b = A,B
    while a !=0:
        temp = a
        a=b%a
        b=temp
    print(A*B//b)
