from Crypto.Cipher import AES
from itertools import product

def encrypt(ptext: str, key: str) -> str:
    ptext, key = bytes.fromhex(ptext), bytes.fromhex(key)
    ctext = AES.new(key, AES.MODE_ECB).encrypt(ptext)
    return ctext.hex().upper()
def decrypt(ptext: str, key: str) -> str:
    ptext, key = bytes.fromhex(ptext), bytes.fromhex(key)
    ctext = AES.new(key, AES.MODE_ECB).decrypt(ptext)
    return ctext.hex().upper()
not_nounce=int(input())
text=input()
text_encrypted=input()
a=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
b=product(a,repeat=not_nounce)
d=dict()
for k in b:
    key1="".join(k)+"0"*(32-not_nounce)
    d[encrypt(text,key1)]=key1
b=product(a,repeat=not_nounce)
for k in b:
    key2="".join(k)+"0"*(32-not_nounce)
    decrypted_once=decrypt(text_encrypted,key2)
    if decrypted_once in d:
        print(d[decrypted_once])
        print(key2)
        break
# 59D04000000000000000000000000000
# FFFFF000000000000000000000000000