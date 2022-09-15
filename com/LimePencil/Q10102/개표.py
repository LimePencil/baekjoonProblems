import sys

input = sys.stdin.readline
n = int(input())
s=input().rstrip()
print("A" if s.count("A")>s.count("B") else ("B" if s.count("A")<s.count("B") else "Tie"))