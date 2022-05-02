from math import log
import sys

input = sys.stdin.readline
for t in range(int(input())):
    print("Data Set {}:".format(t+1))
    e,a=list(map(int,input().split()))
    if e<=a:
        print("no drought")
    else:
        print("mega "*(int(log(e/a-1,5)))+"drought")
    print()