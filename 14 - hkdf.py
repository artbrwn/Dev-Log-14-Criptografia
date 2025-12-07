import os
import jks
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

# Importar la clave desde KeyStore
path = os.path.dirname(__file__)
keystore = os.path.join(path, "files", "KeyStorePracticas")
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave = sk.key

identificador = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

clave_derivada = HKDF(
    master=clave,
    key_len=32,
    salt= bytes.fromhex("00" *64),
    hashmod=SHA512,
    context=identificador
)

clave_hex = clave_derivada.hex().upper()

print(f"La clave es {clave_hex}")