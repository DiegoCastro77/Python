#IF ANIDADOS
#EJEMPLO
"""
Crear un programa que pida un numero, en base a ese numero que imprima el dia de la semana, por ejemplo:
Lunes 1, Martes 2, Miercoles 3, Jueves 4, Viernes 5, Sabado 6, Domingo 7
"""



# Se imprime un encabezado para indicar que se trata de un ejemplo
print("--------EJEMPLO--------")

# Se solicita al usuario que ingrese un número que represente un día de la semana y se convierte a entero
dia = int(input("Ingrese el numero del dia de la semana: "))

# Se inicia una estructura condicional if para determinar el día de la semana
if dia == 1:
    # Si el número ingresado es igual a 1, se imprime "Es lunes"
    print("Es lunes")
else:
    # Si el número ingresado no es igual a 1, se inicia una estructura condicional if anidada
    if dia == 2:
        # Si el número ingresado es igual a 2, se imprime "Es Martes"
        print("Es Martes")
    else:
        # Si el número ingresado no es igual a 2, se inicia otra estructura condicional if anidada
        if dia == 3:
            # Si el número ingresado es igual a 3, se imprime "Es Miercoles"
            print("Es Miercoles")
        else:
            # Si el número ingresado no es igual a 3, se inicia otra estructura condicional if anidada
            if dia == 4:
                # Si el número ingresado es igual a 4, se imprime "Es Jueves"
                print("Es Jueves")
            else:
                # Si el número ingresado no es igual a 4, se inicia otra estructura condicional if anidada
                if dia == 5:
                    # Si el número ingresado es igual a 5, se imprime "Es Viernes"
                    print("Es Viernes")
                else:
                    # Si el número ingresado no es igual a 5, se inicia otra estructura condicional if anidada
                    if dia == 6:
                        # Si el número ingresado es igual a 6, se imprime "Es Sabado"
                        print("Es Sabado")
                    else:
                        # Si el número ingresado no es igual a 6, se inicia otra estructura condicional if anidada
                        if dia == 7:
                            # Si el número ingresado es igual a 7, se imprime "Es Domingo"
                            print("Es Domingo")
                        else:
                            # Si el número ingresado no coincide con ninguno de los días de la semana, se imprime "No ha ingresado un numero correcto"
                            print("No ha ingresado un numero correcto")