import sys
import math

a, b = list(map(int,sys.stdin.readline().strip('\n').rstrip().split(" ")))

print(str(math.gcd(a,b)) +"\n"+ str(math.lcm(a,b)))