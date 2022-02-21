import sys

n = int(input())
m = int(input())

if n>=3 and m<=4:
    print("TroyMartian")
if n<=6 and m>=2:
    print("VladSaturnian")
if n<=2 and m<=3:
    print("GraemeMercurian")