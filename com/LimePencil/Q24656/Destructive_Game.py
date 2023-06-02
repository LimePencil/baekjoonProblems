import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x=0
for _ in range(n):
    a,b = list(map(int,input().split()))    
    if b%2==1:
        x^=a&1
    else:
        r=a%(b+1)
        if r==b:
            x^=2
        else:
            x^=r%2
print("Alice" if x else "Bob")