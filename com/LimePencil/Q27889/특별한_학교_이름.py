import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
if s=="NLCS":
    print("North London Collegiate School")
elif s=="BHA":
    print("Branksome Hall Asia")
elif s=="KIS":
    print("Korea International School")
else:
    print("St. Johnsbury Academy")