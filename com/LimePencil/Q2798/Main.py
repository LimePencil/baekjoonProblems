import sys
from itertools import combinations
_, m = list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" ")))
cards = list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" ")))

combo = list(combinations(cards,3))
sums = 1000000
for c in combo:
    new_sum = sum(list(c))
    if(new_sum <= m and (abs(sums-m) > abs(new_sum-m))):
        sums = new_sum
sys.stdout.write(str(int(sums)))
