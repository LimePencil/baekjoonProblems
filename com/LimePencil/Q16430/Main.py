import sys

a, b = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(str(b-a) + " " + str(b))