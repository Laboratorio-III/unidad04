Documneto = '''
Es importante destacar que, aunque los hashes son resistentes a 
colisiones (es decir, es poco probable que dos conjuntos de datos 
distintos generen el mismo hash), no son reversibles. No se puede 
recuperar la información original a partir del hash, lo que los 
hace útiles para proteger la integridad y la seguridad de los datos.
'''

import hashlib

password = "contraseña"

# Generar un hash utilizando el algoritmo SHA-256
hash_sha256 = hashlib.sha256(password.encode()).hexdigest()

# Generar un hash utilizando el algoritmo SHA-512
hash_sha512 = hashlib.sha512(password.encode()).hexdigest()

# Generar un hash utilizando el algoritmo MD5
hash_md5 = hashlib.md5(Documneto.encode()).hexdigest()

print("Hash con SHA-256:", hash_sha256)
print("Hash con SHA-512:", hash_sha512)
print("Hash con MD5:", hash_md5)

