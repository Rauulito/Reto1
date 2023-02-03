# Definir el alfabeto
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Definir el texto a cifrar
text = "GSVUOZTRHHZBDVZIVXIZAB"

# Inicializar la cadena de texto cifrado
ciphertext = ""

# Iterar cada carácter del texto
for char in text:
    # Obtener el índice del carácter del texto original
    idx = alphabet.find(char)
    # Calcular el índice del carácter cifrado
    ciph_idx = 25 - idx
    # Obtener el carácter cifrado
    ciph_char = alphabet[ciph_idx]
    # Añadir el carácter cifrado a la cadena de texto cifrado
    ciphertext += ciph_char

# Imprimir el texto cifrado
print(ciphertext)