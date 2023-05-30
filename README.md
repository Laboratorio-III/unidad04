# Unidad 4

## Password hashing

Un hash es una función criptográfica que toma una entrada (también conocida como mensaje o datos) y la transforma en una cadena de caracteres de longitud fija. El objetivo principal de una función hash es producir un resumen único y distintivo de los datos de entrada.

Las funciones hash tienen las siguientes características:

1. **Integridad**: Un pequeño cambio en los datos de entrada producirá un hash completamente diferente. Esto permite detectar cualquier alteración en los datos originalmente hashados.

2. **Unidireccionalidad**: Es computacionalmente difícil o casi imposible recuperar los datos de entrada a partir del hash. Esto significa que no se puede reconstruir la información original a partir del resumen generado.

3. **Determinismo**: Dados los mismos datos de entrada, una función hash siempre producirá el mismo resultado de hash. Esto asegura la consistencia en el proceso de hash.

4. **Eficiencia**: Las funciones hash deben ser rápidas de calcular, incluso para grandes cantidades de datos.

Las funciones hash se utilizan en diversos campos, incluyendo la seguridad informática y la verificación de integridad de datos. Algunos casos de uso comunes incluyen:

- **Contraseñas**: En lugar de almacenar las contraseñas en texto plano, se almacena el hash de la contraseña. Esto proporciona una capa adicional de seguridad, ya que incluso si un atacante obtiene acceso a la base de datos de contraseñas, no podrá conocer las contraseñas originales.

- **Verificación de integridad**: Los hashes se utilizan para verificar si los datos se han modificado o dañado durante la transferencia o almacenamiento. Por ejemplo, los archivos descargados a menudo se acompañan de un hash para garantizar que el archivo no haya sido alterado.

- **Detección de duplicados**: Los hashes se pueden utilizar para identificar duplicados en grandes conjuntos de datos sin necesidad de comparar los datos completos. Si dos hashes son idénticos, existe una alta probabilidad de que los datos también lo sean.

Es importante destacar que, aunque los hashes son resistentes a colisiones (es decir, es poco probable que dos conjuntos de datos distintos generen el mismo hash), no son reversibles. No se puede recuperar la información original a partir del hash, lo que los hace útiles para proteger la integridad y la seguridad de los datos.

### Ejemplo

```python
import hashlib

password = "contraseña"

# Generar un hash utilizando el algoritmo SHA-256
hash_sha256 = hashlib.sha256(password.encode()).hexdigest()

# Generar un hash utilizando el algoritmo SHA-512
hash_sha512 = hashlib.sha512(password.encode()).hexdigest()

# Generar un hash utilizando el algoritmo MD5
hash_md5 = hashlib.md5(password.encode()).hexdigest()

print("Hash con SHA-256:", hash_sha256)
print("Hash con SHA-512:", hash_sha512)
print("Hash con MD5:", hash_md5)
```



> 