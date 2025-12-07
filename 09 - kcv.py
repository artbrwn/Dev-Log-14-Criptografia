import hashlib
from Crypto.Cipher import AES

clave_AES = "A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"

m = hashlib.sha256()
m.update(bytes.fromhex(clave_AES))
KCV_SHA_256 = m.digest().hex()[0:6].upper()

print(f"KCV SHA256: {KCV_SHA_256}")

#################################

texto = bytes.fromhex("00" * AES.block_size)
iv = bytes.fromhex("00" * AES.block_size)

cipher = AES.new(bytes.fromhex(clave_AES), AES.MODE_CBC,iv)
KCV_AES = cipher.encrypt(texto).hex()[0:6].upper()

print(f"KCV AES: {KCV_AES}")