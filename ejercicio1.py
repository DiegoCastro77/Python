 #IF ANIDADOS

# Ejemplo de uso de instrucciones if anidadas en Python

# Se imprime un encabezado para el ejemplo
print("---------EJEMPLO---------")

# Se definen algunas variables
nombre = "Diego Castro"
ciudad = "Cucuta"
continente = "Sur America"
edad = 175
mayoria_edad = 18

# Se inicia una estructura condicional if para verificar la edad
if edad >= mayoria_edad:
    # Si la edad es mayor o igual a la mayoría de edad, se imprime un mensaje indicando que la persona es mayor de edad
    print(f"{nombre} es mayor de edad !!")

    # Dentro de este bloque de código, hay otra instrucción if anidada para verificar el continente
    if continente != "Sur America":
        # Si el continente es diferente de "Sur America", se imprime un mensaje indicando que el usuario no es de Sur America
        print("El usuario no es de Sur America")
    else:
        # Si el continente es "Sur America", se imprime un mensaje indicando que es Sur Americano y de la ciudad especificada
        print(f"Es Sur Americano y de {ciudad}")
else:
    # Si la edad no es mayor o igual a la mayoría de edad, se imprime un mensaje indicando que la persona no es mayor de edad
    print(f"{nombre} No es mayor de edad")