import sys
from itertools import permutations

n, d = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
minimum = float('inf')
for i in permutations(range(d),d):
    if i[0] == 0:
        continue
    num = ''.join([str(elem) for elem in i])
    dec = int(num,base=d)
    if dec > n and min(dec,minimum) ==  dec:
        minimum = min(dec,minimum)
print(minimum if minimum != float('inf') else -1)