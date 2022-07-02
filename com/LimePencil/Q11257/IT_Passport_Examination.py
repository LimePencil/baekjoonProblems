import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,a,b,c = list(map(int,input().split()))
    s=a+b+c
    print(n,s, "PASS" if a>=35*0.3 and b>=25*0.3 and c>=40*0.3 and s>=55  else "FAIL")