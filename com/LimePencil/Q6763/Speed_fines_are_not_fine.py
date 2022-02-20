import sys

input = sys.stdin.readline
l = int(input())
s = int(input())
if l-s>=0:
    print("Congratulations, you are within the speed limit!")
elif l-s>=-20:
    print("You are speeding and your fine is $100.")
elif l-s>=-30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")