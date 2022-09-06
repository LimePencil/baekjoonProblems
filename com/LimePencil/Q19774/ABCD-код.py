import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s=input().rstrip()
    
    print("YES" if (int(s[:2])**2+(int(s[2:]))**2)%7==1 else "NO")