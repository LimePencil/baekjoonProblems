import sys

input = sys.stdin.readline
a = int(input())*3+int(input())*2+int(input())
b= int(input())*3+int(input())*2+int(input())
if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("T")