from electrum.bitcoin import script_to_p2wsh
from electrum.crypto import hmac_oneshot
import hashlib
import hmac
import time
from hashlib import _hashlib
from electrum.blockchain import pow_raw_header, bfh, hash_encode, hash_raw_header, pow_raw_header_str, \
    int_to_hex, hash_decode
import tdc_yespower
hex_to_int = lambda s: int.from_bytes(s, byteorder='little')

def nbits(num):
    # Convert integer to hex
    hexstr = format(num, 'x')
    first_byte, last_bytes = hexstr[0:2], hexstr[2:]
    # convert bytes back to int
    first, last = int(first_byte, 16), int(last_bytes, 16)
    return last * 256 ** (first - 3)

def difficulty(num):
    # Difficulty of genesis block / current
    return 0x00ffff0000000000000000000000000000000000000000000000000000 / nbits(num)

def bits(num):
    # Difficulty of genesis block / current
    return target_to_bits(int(0x00ffff0000000000000000000000000000000000000000000000000000 * num))

def to_target(num):
    # Difficulty of genesis block / current
    return int(0x00ffff0000000000000000000000000000000000000000000000000000 * num)


def bits_to_target(bits: int) -> int:
        bitsN = (bits >> 24) & 0xff
        if not (0x03 <= bitsN <= 0x20):
            raise Exception("First part of bits should be in [0x03, 0x1d]")
        bitsBase = bits & 0xffffff
        if not (0x8000 <= bitsBase <= 0x7fffff):
            raise Exception("Second part of bits should be in [0x8000, 0x7fffff]")
        return bitsBase << (8 * (bitsN-3))


def target_to_bits(target: int) -> int:
        c = ("%066x" % target)[2:]
        while c[:2] == '00' and len(c) > 6:
            c = c[2:]
        bitsN, bitsBase = len(c) // 2, int.from_bytes(bfh(c[:6]), byteorder='big')
        if bitsBase >= 0x800000:
            bitsN += 1
            bitsBase >>= 8
        return bitsN << 24 | bitsBase


target = bits_to_target(0x1d032a30)

header = "00000002ba5887e6e6b9e661c5a5b47f4ea42b6ae6a0e4b012d2bf647a4ff426965ebc51fcd95e9b9849f4dcab40c3c3d7c5ce2b660c2104b12f8e64866cf2feba49a2d06246ff141d032a30897415cb"
print(len(header))
block_hash_as_num = int.from_bytes(hash_decode("e1a8f633e37ea32c9b1df2e1102fcae38597f41a00470ec821234dd19c3c0900"), byteorder='big')
print(block_hash_as_num)
print(hash_decode("e1a8f633e37ea32c9b1df2e1102fcae38597f41a00470ec821234dd19c3c0900").hex())
print(pow_raw_header_str(header))
print(hash_encode(tdc_yespower.getPoWHash(bfh(header))))
print(hash_raw_header(header))
print(int.from_bytes(bfh(pow_raw_header_str(header)), byteorder='big'))
print(target_to_bits(int.from_bytes(bfh(pow_raw_header_str(header)), byteorder='big')))
print(len(header))
"56384a672a12de869eb00a253c0ed413741672cb0125049638b6e62e6ccd0000"
if block_hash_as_num < int(1/(0.2/65536)*0x00000000ffff0000000000000000000000000000000000000000000000000000):
    print("ok", block_hash_as_num, int(1/(0.2/65536)*0x00000000ffff0000000000000000000000000000000000000000000000000000))






print()


print(target_to_bits(0x00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff))
print(target_to_bits(0x00000000ffff0000000000000000000000000000000000000000000000000000))
print(target_to_bits(0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff))

print(target_to_bits(target))

print()
print(0x01ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff/target)
print(0x0000ffff)
print((0x1d032a30 & 0x00ffffff))
print(0x0000ffff / (0x1d032a30 & 0x00ffffff))
print(0x0000ffff, 0x1d032a30, 0x00ffffff)
print(0x00000000ffff0000000000000000000000000000000000000000000000000000 / target, 0x00ffffff)

print((0x00000000ffff0000000000000000000000000000000000000000000000000000 / (0.05/65536)))

print(0x00000000ffff0000000000000000000000000000000000000000000000000000 - (int(0x00000000ffff0000000000000000000000000000000000000000000000000000*(0.5/65536))), target)



print(target_to_bits(0x00000000ffff0000000000000000000000000000000000000000000000000000 - (int(0x00000000ffff0000000000000000000000000000000000000000000000000000*(0.5*65536)))))





print()




print(target_to_bits(int(0x00000000ffff0000000000000000000000000000000000000000000000000000 * (0.05*65536))), 0x00ffffff)


print(0x0000ffff / (0x1d032a30 & 0x00ffffff))
print(target_to_bits(int(0x00000000ffff0000000000000000000000000000000000000000000000000000*0.05*65536)))
print(difficulty(0x1d032a30))
print(bits(1/0.05/65536))
print(to_target(0.3159714186530896))
print(bits_to_target(0x1d032a30))

print(int(1/(0.3159714186530896)*0x00000000ffff0000000000000000000000000000000000000000000000000000))
print(int(1/(0.05/65536)*0x00000000ffff0000000000000000000000000000000000000000000000000000))
print(target_to_bits(int(1/(0.05/65536)*0x00000000ffff0000000000000000000000000000000000000000000000000000)))

print(hex_to_int(b"5dc79ab9"))

print(int_to_hex(4134974306249827381))
