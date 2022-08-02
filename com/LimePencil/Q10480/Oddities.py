import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())

    print("{} is {}".format(n,"odd" if n%2 else "even"))