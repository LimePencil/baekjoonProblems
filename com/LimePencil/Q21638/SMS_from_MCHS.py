a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))
if c <0 and d>=10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif c<a:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif d>b:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")