import sys

print(*map(str,sorted(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))))