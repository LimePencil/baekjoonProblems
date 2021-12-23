import sys

total = int(sys.stdin.readline().rstrip("\n"))
diff = int(sys.stdin.readline().rstrip("\n"))
one = (total-diff)//2
two = one + diff
print(two)
print(one)
