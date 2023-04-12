##################################################################
#   Crear una aplicacion que implemente: suma, resta, multiplicacion y division de n numeros.
#   Validar los numeros por parametros para los numeros

######  Principal   ######

print("Sumas, resta, multiplicacion y division de n numeros:")   #Titulo del programa

def Menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = int(print("Ingrese opcion: \n"))
    return opcion
    

#validacion
n = int(print("Ingrese n: "))    #Ingreso de la cantidad de numeros a operar
Operacion = Menu()





























def suma_numeros(numeros):
    return sum(numeros)

def resta_numeros(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado -= numeros[i]
    return resultado

def multiplicacion_numeros(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def division_numeros(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] == 0:
            print("Error: No se puede dividir por cero")
            return None
        resultado /= numeros[i]
    return resultado

operaciones = {
    "1": suma_numeros,
    "2": resta_numeros,
    "3": multiplicacion_numeros,
    "4": division_numeros
}

while True:
    print("\nIngrese una lista de números separados por comas (ejemplo: 1,2,3):")
    numeros = input().split(",")
    numeros = [float(num) for num in numeros]
    print("\nSeleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operacion = input()
    resultado = operaciones.get(operacion)(numeros)
    if resultado is not None:
        print("\nEl resultado de la operación es:", resultado)
    print("\n¿Desea realizar otra operación? (s/n)")
    continuar = input()
    if continuar.lower() != "s":
        break