d = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0,"B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3,"D0": 1.0, "D-": 0.7, "F": 0.0}
s=0
p=0
for _ in range(int(input())):
    a=input().split()
    s+=d[a[2]]*int(a[1])
    p+=int(a[1])
print("{:.2f}".format(s/p+10**-10))