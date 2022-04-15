from Crypto.Cipher import AES
from itertools import product

def encrypt(ptext: str, key: str) -> str:
    ptext, key = bytes.fromhex(ptext), bytes.fromhex(key)
    ctext = AES.new(key, AES.MODE_ECB).encrypt(ptext)
    return ctext.hex().upper()
not_nounce=int(input())
text=input()
text_encrypted=input()
a=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
b=product(a,repeat=not_nounce*2)
for k in b:
    key1="".join(k[:not_nounce])+"0"*(32-not_nounce)
    key2="".join(k[not_nounce:])+"0"*(32-not_nounce)
    s=encrypt(encrypt(text, key1),key2)
    if s==text_encrypted:
        print(key1)
        print(key2)

# A7000000000000000000000000000000
# 6E000000000000000000000000000000