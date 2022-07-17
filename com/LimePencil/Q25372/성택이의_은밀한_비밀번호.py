import sys

input = sys.stdin.readline
for _ in range(int(input())):
    print("yes" if 6<=len(input().rstrip())<=9 else "no")