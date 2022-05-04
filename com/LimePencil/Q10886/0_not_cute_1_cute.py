import sys

input = sys.stdin.readline
n = int(input())
print("Junhee is not cute!" if sum([int(input()) for _ in range(n)])<n/2 else  "Junhee is cute!")