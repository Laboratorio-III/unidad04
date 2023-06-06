def complex_hash(data):
    hash_value = 0
    prime = 31

    for char in data:
        hash_value = hash_value * prime + ord(char) & 0xFFFFFFFF

    return hash_value


# Ejemplo de uso
data = "Hola. mundo!"

hash_result = complex_hash(data)
print("Hash generado:", hash_result)