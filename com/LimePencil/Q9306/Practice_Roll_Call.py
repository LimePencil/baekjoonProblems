import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [input()  for _ in range(n*2)]
for i in range(n):
    print(f"Case {i+1}: {arr[2*i+1]}, {arr[2*i]}")