import os
import jks
from Crypto.Hash import HMAC, SHA256

mensaje = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf-8")


# Importar la clave desde KeyStore
path = os.path.dirname(__file__)
keystore = os.path.join(path, "files", "KeyStorePracticas")
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "hmac-sha256":
        clave = sk.key

hmac256 = HMAC.new(clave, msg=mensaje, digestmod=SHA256)
print(hmac256.hexdigest().upper())