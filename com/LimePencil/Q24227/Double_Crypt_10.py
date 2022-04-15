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
s=int(input())
text=input()
text_encrypted=input()
hex_values=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
poss_keys=product(hex_values,repeat=s)
encrypted_once=dict()
for k in poss_keys:
    key1="".join(k)+"0"*(32-s)
    encrypted_once[encrypt(text,key1)]=key1
poss_keys=product(hex_values,repeat=s)
for k in poss_keys:
    key2="".join(k)+"0"*(32-s)
    decrypted_once=decrypt(text_encrypted,key2)
    if decrypted_once in encrypted_once:
        print(encrypted_once[decrypted_once])
        print(key2)
        break
# 59D04000000000000000000000000000
# FFFFF000000000000000000000000000