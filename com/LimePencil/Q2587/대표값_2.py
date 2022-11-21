import sys
import statistics
input = lambda: sys.stdin.readline().rstrip()
arr = [int(input()) for _ in range(5)]
print(statistics.mean(arr))
print(statistics.median(arr))