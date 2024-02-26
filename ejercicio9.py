# Parte 1: Utilizando un bucle while
contador = 1 # Inicializamos el contador en 1

print("\a \n---------------- Ciclo while ----------------")

while contador < 61:  # Mientras el contador sea menor que 61
    cuadrado = contador * contador  # Calculamos el cuadrado del contador
    print(f" \n \a El cuadrado de {contador} es {cuadrado}\n")  # Imprimimos el cuadrado del contador
    contador += 1  # Incrementamos el contador en 1 en cada iteración

print("\a \n---------------- Ciclo for ----------------")

# Parte 2: Utilizando un bucle for
for numero in range(1, 61):  # Iteramos sobre los números del 0 al 60
    contador = numero * numero  # Calculamos el cuadrado del número actual
    print(f"\n \a El cuadrado de {numero} es {contador}")  # Imprimimos el cuadrado del número actual