import sys

input = sys.stdin.readline
people = [input().rstrip() for _ in range(int(input()))]
print("뭐야;" if "anj" in people else "뭐야?")