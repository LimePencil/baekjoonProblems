import sys

input = lambda: sys.stdin.readline().rstrip()
arr = [len(input()) for _ in range(6)]
print(f"Latitude {arr[0]}:{arr[1]}:{arr[2]}")
print(f"Longitude {arr[3]}:{arr[4]}:{arr[5]}")