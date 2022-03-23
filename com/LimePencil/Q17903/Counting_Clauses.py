import sys

input = sys.stdin.readline
n,m= list(map(int,input().split()))
print("unsatisfactory" if n<8 else "satisfactory")