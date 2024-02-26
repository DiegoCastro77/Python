numero = int(input("Introduce el número: "))

porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}? "))

# Se calcula el porcentaje del número ingresado por el usuario
operacion = (numero * (porcentaje / 100))

# Se imprime el resultado del cálculo del porcentaje
print(f"El {porcentaje}% de {numero} es: {operacion}")
