import sys

input = sys.stdin.readline
students=set(range(1,31))
for _ in range(28):
    students.remove(int(input()))
print(*sorted(list(students)),sep="\n")