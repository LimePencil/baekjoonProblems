import sys

n,m,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(str(k//m) + " " + str(k%m))