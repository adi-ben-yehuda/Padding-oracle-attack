from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad,unpad
import sys
import binascii

#E
def xor(a, b, c):
    res = a ^ b ^ c
    return res.to_bytes(1, 'little')


#F
def oracle(ciphertext, KEY, IV):
    crypter = DES.new(KEY, DES.MODE_CBC, IV)
    plain_text = crypter.decrypt(ciphertext)
    padding_length = plain_text[-1]
    if padding_length > len(plain_text) or padding_length == 0:
        return False
    expected_padding = bytes([padding_length]) * padding_length
    return plain_text[-padding_length:] == expected_padding


if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) < 4:
        exit(1)

    # ciphertext = bytes.fromhex("4e301349b6704658fcb5fb7dabf34e206e3e1223b86c1b4e360d69dcac04ac4e")
    # KEY = bytes("Aalenian".encode())
    # IV = bytes.fromhex("8487ffc596953c48")

    ciphertext = bytes.fromhex(arguments[1])
    KEY = bytes(arguments[2].encode())
    IV = bytes.fromhex(arguments[3])

    final_plain_text = b''
    numOfBlocks = int(len(ciphertext) / 8)
    zeros = bytearray(8)

    for k in range(numOfBlocks):
        c = zeros + ciphertext[k * 8:(k+1)*8]
        block = b''
        for i in reversed(range(8)):
            while (oracle(c, KEY, IV) == False):
                mutable_bytes = bytearray(c)
                mutable_bytes[i] += 1
                c = bytes(mutable_bytes)

            if (k==0):
                x = xor(8-i, bytearray(c)[i], bytearray(IV)[i])
            else:
                x = xor(8-i, bytearray(c)[i], bytearray(ciphertext)[i+(k-1)*8])
            block = x+ block

            mutable_bytes1 = bytearray(c)
            for j in range(i, 8):
                if (k==0):
                    x1 = xor(block[j-i], 9-i, bytearray(IV)[j])
                else:
                    x1 = xor(block[j-i], 9-i, bytearray(ciphertext)[j+(k-1)*8])
                mutable_bytes1[j] = bytes.fromhex(x1.hex())[0]
            c = bytes(mutable_bytes1)
        final_plain_text = final_plain_text + block

    decrypt_plain_text = bytes(unpad(final_plain_text, DES.block_size))
    print(decrypt_plain_text.decode())
