print("--------Ejemplo--------")

# Se solicita al usuario que ingrese un número para generar la tabla de multiplicar.
numero_usuario = int(input("¿De qué número quieres la tabla?"))

# Se imprime el encabezado de la tabla de multiplicar con el número ingresado por el usuario.
print(f"----Tabla del {numero_usuario}----")

# Se inicializa un contador que comenzará desde 1.
contador = 1

# Se inicia un bucle while que se ejecutará mientras el contador sea menor o igual a 10.
while contador <= 10:
    # En cada iteración, se imprime la multiplicación del número ingresado por el usuario y el contador.
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    # Se incrementa el contador en 1 para pasar al siguiente número.
    contador += 1
# Una vez que el bucle while termina (cuando el contador es mayor que 10),
# se ejecuta el bloque de código dentro del else.
else:
    # Se imprime un mensaje indicando que la tabla ha terminado.
    print("Tabla terminada.")
