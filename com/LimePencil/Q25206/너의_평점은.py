import sys

input = sys.stdin.readline
total_credit=0
total_point=0
for _ in range(20):
    name,credit,grade = input().split()
    credit=float(credit)
    if grade=="P":
        continue
    total_credit+=credit
    if grade=="A+":
        grade=4.5
    elif grade=="A0":
        grade=4.0
    elif grade=="B+":
        grade=3.5
    elif grade=="B0":
        grade=3
    elif grade=="C+":
        grade=2.5
    elif grade=="C0":
        grade=2
    elif grade=="D+":
        grade=1.5
    elif grade=="D0":
        grade=1
    else:
        grade=0
    total_point+=grade*credit
print(total_point/total_credit)