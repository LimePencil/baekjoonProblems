import sys

a1, b1, c1 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
a2, b2, c2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

print(str(a2-c1) + " "+ str(b2//b1) + " " + str(c2-a1))