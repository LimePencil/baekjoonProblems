import sys

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    stickers = []
    column = int(sys.stdin.readline().rstrip("\n"))
    values = [[0 for _ in range(column+1)]for _ in range(2)]
    for i in range(2):
        stickers.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
    for i in range(column+1):
        if i==0:
            continue
        elif i ==1:
            values[0][i] = stickers[0][i-1]
            values[1][i] = stickers[1][i-1]
        else:
            values[0][i] = max(values[1][i-1],values[1][i-2]) + stickers[0][i-1]
            values[1][i] = max(values[0][i-1],values[0][i-2]) + stickers[1][i-1]
            
    print(max(values[0][column],values[1][column]))
