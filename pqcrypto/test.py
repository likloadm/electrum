import pqcrypto
import os, binascii

import hashlib



salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')

passwd = "it@aosvet.com;poiouieyw4ty7uy39jik01douihtubg43y2ido4uijyetefhu".encode("utf8")
key = hashlib.pbkdf2_hmac('sha512', passwd, b'aaef2d3f4d77ac66e9c5a6c3d8f921d1', iterations=500000, dklen=48)

print("Derived key:", binascii.hexlify(key))


x=pqcrypto.crypto_sign_keypair(key)
print(x.hex())