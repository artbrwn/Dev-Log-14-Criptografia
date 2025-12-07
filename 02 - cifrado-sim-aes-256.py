from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import os
import jks

# Importar la clave desde KeyStore
path = os.path.dirname(__file__)
keystore = os.path.join(path, "files", "KeyStorePracticas")
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave = sk.key

iv = bytes.fromhex("00" * AES.block_size)

# Decodificar el dato cifrado de base64 a binario
dato_cifrado = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
dato_cifrado_binario = b64decode(dato_cifrado)

# Crear descifrador
descifrador = AES.new(clave, AES.MODE_CBC, iv)

# Descifrar el texto
dato_descifrado = descifrador.decrypt(dato_cifrado_binario)
print(f"El texto descifrado con padding es: {dato_descifrado}")

# Eliminar padding
dato_sin_padding = unpad(dato_descifrado, AES.block_size)

# Decodificar a string
texto = dato_sin_padding.decode("utf-8")

print(f"El texto descifrado es: {texto}")

# Cambio estilo padding
dato_sin_padding_incorrecto = unpad(dato_descifrado, AES.block_size, style="x923")
texto = dato_sin_padding_incorrecto.decode("utf-8")
print(f"El texto descifrado con el padding x923 es: {texto}")

longitud_padding = dato_descifrado.hex()[-1]

print(f"La longitud del padding es: {longitud_padding}")