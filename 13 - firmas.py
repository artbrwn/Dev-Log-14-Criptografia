from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import os

# Obtenemos la firma
my_path = os.path.abspath(os.getcwd())
path_file_priv = os.path.join(my_path, "files","clave-rsa-oaep-priv.pem")
keypriv = RSA.importKey(open(path_file_priv).read())

# Hasheamos el mensaje
mensaje_bytes = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
hash = SHA256.new(mensaje_bytes)

# Creamos el "firmador" y firmamos
firmador=PKCS115_SigScheme(keypriv)
firma = firmador.sign(hash)
print(f"La firma es: {firma.hex().upper()}")


# VERIFICAMOS LA FIRMA

mensaje_bytes_verif = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","utf-8")
h = SHA256.new(mensaje_bytes_verif)

pub = RSA.import_key(open(os.path.join(my_path, "files","clave-rsa-oaep-publ.pem")).read())
verificador = PKCS115_SigScheme(pub)

try:
    verificador.verify(h, firma)
    print("Firma correcta")
except (ValueError, TypeError):
    print("Firma inválida")


#################################################


from nacl.signing import SigningKey, VerifyKey

my_path = os.path.abspath(os.getcwd())
path_file_priv = os.path.join(my_path, "files","ed25519-priv")

with open(path_file_priv, "rb") as f:
    priv_bytes = f.read()

# Creamos el "firmador"
# Los primeros 32 bytes son la semilla el resto es la clave pública.
seed = priv_bytes[:32]
sk = SigningKey(seed)

# Firmamos y obtenemos la clave
firmado = sk.sign(mensaje_bytes)
firma = firmado.signature
print(f"La firma es {firma.hex().upper()}")


# VERIFICAMOS LA FIRMA
# Leemos clave pública
path_file_priv = os.path.join(my_path, "files","ed25519-publ")
with open(path_file_priv , "rb") as f:
    pub_bytes = f.read()
    
# Creamos verificador
vk = VerifyKey(pub_bytes)

try:
    vk.verify(mensaje_bytes, firma)
    print("Firma correcta")
except (ValueError, TypeError):
    print("Firma inválida")
