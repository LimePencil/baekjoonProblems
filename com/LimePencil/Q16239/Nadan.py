import sys

input = sys.stdin.readline
k = int(input())
n = int(input())
for i in range(1,n):
    k-=i
    print(i)
print(k)