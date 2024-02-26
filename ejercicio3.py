# Se solicita al usuario que ingrese un país
pais = input("Ingrese un país: ")

# Se verifica si el país ingresado está dentro de los países de habla hispana
if pais == "mexico" or pais == "españa" or pais == "colombia": 
    # Si el país está en la lista, se imprime que es un país de habla hispana
    print(f"{pais} es un país de habla hispana")
else:
    # Si el país no está en la lista, se imprime que no es un país de habla hispana
    print(f"{pais} no es un país de habla hispana")

# Se corrige la condición en el siguiente bloque de código
# Se verifica si el país ingresado no está dentro de los países de habla hispana
if not (pais == "mexico" or pais == "españa" or pais == "colombia"): 
    # Si el país no está en la lista, se imprime que no es un país de habla hispana
    print(f"{pais} no es un país de habla hispana")
else:
    # Si el país está en la lista, se imprime que es un país de habla hispana
    print(f"{pais} sí es un país de habla hispana")

# Se corrige la condición en el último bloque de código
# Se verifica si el país ingresado no está dentro de los países de habla hispana
if pais != "mexico" and pais != "españa" and pais != "colombia": 
    # Si el país no está en la lista, se imprime que no es un país de habla hispana
    print(f"{pais} no es un país de habla hispana")
else:
    # Si el país está en la lista, se imprime que es un país de habla hispana
    print(f"{pais} sí es un país de habla hispana")
