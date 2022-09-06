import sys

input = sys.stdin.readline
x,k,a = list(map(int,input().split()))
print("1" if x%(k+a)<k else "0")