from math import comb
import sys
n, k = list(map(int, sys.stdin.readline().strip('\n').rstrip().split(" ")))
sys.stdout.write(str(comb(n,k)))