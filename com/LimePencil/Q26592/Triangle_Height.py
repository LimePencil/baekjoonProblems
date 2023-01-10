import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,b= list(map(float,input().split()))
    print(f"The height of the triangle is {2*a/b:.2f} units")