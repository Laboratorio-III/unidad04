# Unidad 4

## Hashing

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

## Ejercicio 1
---
El algoritmo de hash más simple se conoce como "hashing sin criptografía" o "hashing no seguro". Este tipo de algoritmo no está diseñado para la seguridad, sino más bien para la velocidad y la simplicidad. No se recomienda utilizarlo en aplicaciones donde se requiere una seguridad adecuada, ya que es más susceptible a colisiones y ataques de fuerza bruta.

### El algoritmo

* Inicializa una variable para almacenar el valor hash.
* Recorre los caracteres de la entrada de datos.
* Para cada carácter, conviértelo en un valor numérico.
* Agrega el valor numérico al valor hash existente.
* Continúa recorriendo y sumando los valores numéricos de los caracteres hasta que hayas procesado todos los caracteres de la entrada de datos.
* Devuelve el valor hash resultante.

## Ejercicio 1
---
Desarrolla una función en Python llamada complex_hash que tome una cadena de texto como entrada y aplique un algoritmo de hashing por multiplicación para generar un valor hash único. A continuación, se describen los pasos del algoritmo:

Define una función llamada complex_hash que tome una cadena de texto como parámetro de entrada.

- Inicializa una variable llamada hash_value en 0 para almacenar el valor hash resultante.
- Elige un número primo, en este caso, el número 31, como constante. Este número ayudará a distribuir mejor los valores hash generados.
- Recorre cada carácter de la cadena de texto utilizando un bucle. Para cada carácter, realiza los siguientes pasos:
    1. Multiplica el valor hash actual, hash_value, por la constante.
    2. Suma el valor numérico del carácter actual utilizando la función ord() para obtener su representación numérica.
    3. Realiza una operación AND entre el resultado de la suma y 0xFFFFFFFF para limitar el valor hash a 32 bits.
    4. Asigna el resultado de la operación anterior a la variable hash_value.
- Una vez se hayan recorrido todos los caracteres de la cadena de texto, retorna el valor hash resultante almacenado en la variable hash_value.
- Ejecuta un ejemplo utilizando la cadena de texto "Hola, mundo!" y almacena el valor hash resultante en una variable llamada hash_result.
- Imprime en pantalla el valor hash resultante utilizando la sentencia print.