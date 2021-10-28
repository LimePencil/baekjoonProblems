import sys

jiphap = set([])
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().strip('\n').split(" ")
    if(command[0] == "add"):
        jiphap.add(int(command[1]))
    elif(command[0] == "remove"):
        jiphap.discard(int(command[1]))
    elif(command[0] == "check"):
        print("1" if int(command[1]) in jiphap else "0")
    elif(command[0] == "empty"):
        jiphap.clear()
    elif(command[0] == "all"):
        jiphap = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif(command[0] == "toggle"):
        if int(command[1]) in jiphap:
            jiphap.discard(int(command[1]))
        else:
            jiphap.add(int(command[1]))
        