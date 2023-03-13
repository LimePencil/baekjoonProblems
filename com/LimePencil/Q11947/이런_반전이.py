import sys

input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n = int(input())
    l= len(str(n))
    highest_in_the_length=int("4"+"9"*(l-1))
    if n>=highest_in_the_length:
        print(highest_in_the_length*(int("9"*l)-highest_in_the_length))
    else:
        print(n*(int("9"*l)-n))