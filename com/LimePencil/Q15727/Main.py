import sys

n = int(sys.stdin.readline().rstrip("\n"))
print(n//5+1 if n%5 !=0 else n//5)