def simple_hash(data):
    hash_value = 0

    for char in data:
        hash_value += ord(char)

    return hash_value


# Ejemplo de uso
data = "Inicializa una variable para almacenar el valor hash."

hash_result = simple_hash(data)
print("Hash generado:", hash_result)