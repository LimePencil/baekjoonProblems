import sys

input = lambda: sys.stdin.readline().rstrip()
w = float(input())
h = float(input())
n=w/h**2
if n>25:
    print("Overweight")
elif n>18.5:
    print("Normal weight")
else:
    print("Underweight")