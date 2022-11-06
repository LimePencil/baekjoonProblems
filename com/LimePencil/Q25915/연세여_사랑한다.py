import sys

input = lambda: sys.stdin.readline().rstrip()
c=input()
print(abs(ord("I")-ord(c))+84)