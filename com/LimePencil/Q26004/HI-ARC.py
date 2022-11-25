import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=input()
print(min(s.count("H"),s.count("I"),s.count("A"),s.count("R"),s.count("C")))