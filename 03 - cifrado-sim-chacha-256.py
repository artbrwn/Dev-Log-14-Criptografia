import os
import jks
from base64 import b64decode, b64encode
from Crypto.Cipher import ChaCha20_Poly1305

# Importar la clave desde KeyStore
path = os.path.dirname(__file__)
keystore = os.path.join(path, "files", "KeyStorePracticas")
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-chacha20-256":
        clave = sk.key

texto = bytes("KeepCoding te enseña a codificar y a cifrar", "utf-8")

nonce = b64decode("9Yccn/f5nJJhAt2S")

cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce)

# Añadimos los datos asociados

aad = bytes("Usuario: Keepcoding", "utf-8")
cipher.update(aad)

texto_cifrado, tag = cipher.encrypt_and_digest(texto)

# Codificamos en base64

texto_cifrado_b64 = b64encode(texto_cifrado)
tag_b64 = b64encode(tag)

print(f"El texto cifrado es: {texto_cifrado_b64}")
print(f"El MAC es: {tag_b64}")