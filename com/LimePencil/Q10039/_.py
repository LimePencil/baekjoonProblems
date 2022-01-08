import sys

total = 0
for _ in range(5):
    n = int(sys.stdin.readline().rstrip("\n"))
    total += max(n,40)
print(total//5)
    