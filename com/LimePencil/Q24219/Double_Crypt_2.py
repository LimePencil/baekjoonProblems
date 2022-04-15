from Crypto.Cipher import AES
from itertools import product

def encrypt(ptext: str, key: str) -> str:
    ptext, key = bytes.fromhex(ptext), bytes.fromhex(key)
    ctext = AES.new(key, AES.MODE_ECB).encrypt(ptext)
    return ctext.hex().upper()

a=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
b=product(a,repeat=4)
for k1,k2,k3,k4 in b:
    key1=k1+k2+"0"*30
    key2=k3+k4+"0"*30
    s=encrypt(encrypt("3FCFAA530B83FAC26C3AF18C958F0665", key1),key2)
    if s=="68F4005C13000809D9F5F090C36FD0F2":
        print(key1)
        print(key2)

# C0000000000000000000000000000000
# 50000000000000000000000000000000