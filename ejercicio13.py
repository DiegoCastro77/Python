numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce el siguiente número: "))

# Se verifica si el primer número es menor que el segundo número
if numero1 < numero2:
    # Si el primer número es menor que el segundo número, se ejecuta el siguiente bloque de código
    # Se itera sobre los números desde el primer número hasta el segundo número (incluido)
    for x in range(numero1, (numero2 + 1)):

        # Se verifica si el número actual es par o impar
        if x % 2 == 0:
            # Si el número es par, se imprime un mensaje indicando que es par
            print(f"{x} es PAR")
        else:
            # Si el número es impar, se imprime un mensaje indicando que es impar
            print(f"{x} es IMPAR")
else:
    # Si el primer número no es menor que el segundo número, se imprime un mensaje indicando que el primer número debe ser mayor al segundo número
    print("El número 1 debe ser menor al número 2")
