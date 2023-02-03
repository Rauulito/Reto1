#CIFRADO atbash

# alfabetos empleados
CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'GSVUOZTRHHZBDVZIVXIZAB '

# Almacena las formas de cifradas y descifradas
salida = ''

# Guarda el texto introducido
texto = input ('introduce un texto: ')

# Ejecuta el cifrado
for simbolo in texto.lower () :
    if simbolo in CLARO:
  
       # Identifica la posición de cada simbolo
       indice = CLARO.index(simbolo)
       salida += CIFRADO [indice]
       
# imprime en pantalla el resultado
print (salida)