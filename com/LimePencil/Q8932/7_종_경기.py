import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a,b,c,d,e,f,g=list(map(int,input().split()))
    print(sum([int(9.23076*abs(26.7-a)**1.835),int(1.84523*abs(75-b)**1.348),int(56.0211*abs(1.5-c)**1.05),int(4.99087*abs(42.5-d)**1.81),int(0.188807*abs(210-e)**1.41),int(15.9803*abs(3.8-f)**1.04),	int(0.11193*abs(254-g)**1.88)]))
