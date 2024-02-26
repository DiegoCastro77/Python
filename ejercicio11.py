# Se solicita al usuario que ingrese dos números enteros
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# Se verifica si el primer número es menor que el segundo número
if numero1 < numero2:
    # Si el primer número es menor que el segundo número, se ejecuta el siguiente bloque de código
    # Se utiliza un bucle for para iterar desde el primer número hasta el segundo número (incluido)
    for contador in range(numero1, (numero2 + 1)):
        # Se imprime cada número en el rango especificado
        print(contador)
else:
    # Si el primer número no es menor que el segundo número, se imprime un mensaje indicando que el primer número debe ser menor que el segundo número
    print("El número 1 debe ser menor al número 2")
