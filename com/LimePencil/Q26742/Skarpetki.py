import sys

input = lambda: sys.stdin.readline().rstrip()
s= input()
print(s.count("B")//2+s.count("C")//2)