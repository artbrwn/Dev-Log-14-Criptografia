def xor(binary_data_1: bytes, binary_data_2: bytes) -> bytes:
    """
    Recibe dos binarios y devuelve el resultado de aplicarles XOR.
    """
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

# Claves introducidas
clave_fija = bytes.fromhex("B1EF2ACFE2BAEEFF")
clave_final = bytes.fromhex("91BA13BA21AABB12")

clave_propiedades = xor(clave_fija, clave_final).hex().upper()

print(f"La clave introducida en el archivo de propiedades es: {clave_propiedades}")

# Claves introducidas
clave_fija = bytes.fromhex("B1EF2ACFE2BAEEFF")
clave_propiedades = bytes.fromhex("B98A15BA31AEBB3F")

clave_final = xor(clave_fija, clave_propiedades).hex().upper()

print(f"La clave final es: {clave_final}")