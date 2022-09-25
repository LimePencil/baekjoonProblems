import sys
import string
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    s=set(input())
    alpha=set(string.ascii_uppercase)
    x=alpha-s
    print(sum([ord(i) for i in x]))