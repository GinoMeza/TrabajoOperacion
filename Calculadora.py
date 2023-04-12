##################################################################
#   Crear una aplicacion que implemente: suma, resta, multiplicacion y division de n numeros.
#   Validar los numeros por parametros para los numeros

def Menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    Opc = int(input(f"Ingrese opcion: \n"))
    return Opc

def Suma(n):
    SumaTotal = 0
    for i in range(0,n):
        SumaTotal = SumaTotal + int(input(f"Ingrese {i+1} numero: \n"))
    return SumaTotal
    
######  Principal   ######
print("Sumas, resta, multiplicacion y division de n numeros:")   #Titulo del programa

#validacion

n = int(input("Ingrese cantidad de numeros a operar: "))    #Ingreso de la cantidad de numeros a operar
Operacion = Menu()
while Operacion < 5 and Operacion > 0:
    if Operacion == 1:
        print(f"La suma es: {Suma(n)}")












