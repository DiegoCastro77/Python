# Se itera sobre los números del 1 al 10 para generar las tablas de multiplicar
for cabecera in range(1, 11):
    print("--------------------------------------")
    print(f"-------------Tabla del {cabecera}--------------")
    print("--------------------------------------")

    # Se itera sobre los números del 1 al 10 para calcular y mostrar las multiplicaciones
    for numero in range(1, 11):
        # Se imprime la multiplicación actual
        print(f"{numero} x {cabecera} = {numero * cabecera}")
    print("\n")
