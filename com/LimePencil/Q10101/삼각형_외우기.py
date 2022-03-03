import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
if a+b+c != 180:
    print("Error")
else:
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")