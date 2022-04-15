from Crypto.Cipher import AES
from itertools import product

def encrypt(ptext: str, key: str) -> str:
    ptext, key = bytes.fromhex(ptext), bytes.fromhex(key)
    ctext = AES.new(key, AES.MODE_ECB).encrypt(ptext)
    return ctext.hex().upper()

s=int(input())
text=input()
text_encrypted=input()
hex_values=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
possible_keys=product(hex_values,repeat=s*2)
for k in possible_keys:
    key1="".join(k[:s])+"0"*(32-s)
    key2="".join(k[s:])+"0"*(32-s)
    encrypted_outcome=encrypt(encrypt(text, key1),key2)
    if encrypted_outcome==text_encrypted:
        print(key1)
        print(key2)

# A7000000000000000000000000000000
# 6E000000000000000000000000000000