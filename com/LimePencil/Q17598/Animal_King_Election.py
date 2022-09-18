import sys

input = lambda: sys.stdin.readline().rstrip()
arr = [input() for _ in range(9)]
print("Tiger" if arr.count("Tiger")>4 else "Lion")
