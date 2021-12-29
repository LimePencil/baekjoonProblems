import sys

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    cloth_num = int(sys.stdin.readline().rstrip("\n"))
    cloths = {}
    for _ in range(cloth_num):
        _,type = sys.stdin.readline().rstrip("\n").split(" ")
        if type in cloths:
            cloths[type] +=1
        else:
            cloths[type] = 1
    total = 1
    for k,v in cloths.items():
        total *=(v+1)
    total -=1
    print(total)