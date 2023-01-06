while True:
    try:
        s=input()
        s=s.replace("e","0")
        s=s.replace("i","e")
        s=s.replace("0","i")
        s=s.replace("E","0")
        s=s.replace("I","E")
        s=s.replace("0","I")
        print(s)
    except:
        break