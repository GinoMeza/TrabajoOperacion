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
    Opc = int(input("Ingrese opcion: \n"))
    return Opc
    

#validacion
n = int(input("Ingrese n: "))    #Ingreso de la cantidad de numeros a operar
Operacion = Menu()













