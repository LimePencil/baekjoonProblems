import sys

input = sys.stdin.readline
l="BCBCDCDADABA"
for _ in range(int(input())):
    n = int(input())
    if n ==1:
        print("A")
    else:
        print(l[(n-2)%12])