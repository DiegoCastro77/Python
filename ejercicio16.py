# Se inicializan las variables contador, aprobados y reprobados
contador = 1
aprobados = 0
reprobados = 0

# Se solicita al usuario que ingrese la cantidad de aprendices
numero_alumnos = int(input("¿Cuántos aprendices tienes?: "))

# Se inicia un bucle while para solicitar las notas de cada aprendiz
while contador <= numero_alumnos:
    # Se solicita al usuario que ingrese la nota del aprendiz actual
    nota = int(input(f"¿Qué nota quiere ponerle al aprendiz {contador}?: "))
    
    # Se verifica si la nota es mayor o igual a 3 para determinar si el aprendiz aprobó o reprobó
    if nota >= 3:
        aprobados += 1  # Se incrementa el contador de aprobados en 1
    else:
        reprobados += 1  # Se incrementa el contador de reprobados en 1
    
    contador += 1  # Se incrementa el contador de aprendices en 1 para pasar al siguiente aprendiz

# Se imprime la cantidad de aprendices aprobados y reprobados
print(f"Aprendices Aprobados: {aprobados}")
print(f"Aprendices Reprobados: {reprobados}")
