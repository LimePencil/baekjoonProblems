import sys

seats = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(seats[0]*seats[1]+seats[2]*seats[3])