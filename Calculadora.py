##################################################################
#   Crear una aplicacion que implemente: suma, resta, multiplicacion y division de numeros.
#   Validar los numeros por parametros para los numeros

def Menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    Opc = int(input(f"Ingrese opcion: \n"))
    while(Opc < 1 and Opc > 5):
        Opc = int(input(f"ERROR! Opcion solo 1 a 5, ingrese nuevamente: \n"))
    return Opc

def Suma(n):
    SumaTotal = 0
    for i in range(0,n):
        SumaTotal = SumaTotal + int(input(f"Ingrese {i+1} numero: \n"))
    return SumaTotal
    
def Resta(n):
    Diferencia = 0
    for i in range(0,n):
        Diferencia = Diferencia - int(input(f"Ingrese {i+1} numero: \n"))
    return Diferencia

def Multiplicacion(n):
    Producto = 0
    for i in range(0,n):
        Producto = Producto * int(input(f"Ingrese {i+1} numero: \n"))
    return Producto

def Division():
    Dividendo = int(input(f"Ingrese dividendo: \n"))
    Divisor = int(input(f"Ingrese divisor(diferente a 0):\n"))
    while(Divisor == 0):
        Divisor = int(input(f"ERROR! Dividendo no debe ser 0, ingrese nuevamente: \n"))
    Cociente = Dividendo/Divisor
    return Cociente


######  Principal   ######
print(f"********            Sumas, resta y multiplicacion de n numeros y division de 2 numeros           **********\n\n")   #Titulo del programa

#validacion

Operacion = Menu()
if Operacion != 4:
    n = int(input(f"\nIngrese cantidad de numeros a operar(Suma, resta, multiplicacion): \n"))    #Ingreso de la cantidad de numeros a operar


while Operacion != 5:
    if Operacion == 1:
        print(f"La suma es: {Suma(n)}\n\n")
    elif Operacion == 2:
        print(f"La resta es: {Resta(n)}\n\n")
    elif Operacion == 3:
        print(f"La multiplicacion es: {Multiplicacion(n)}\n\n")
    elif Operacion == 4:
        print(f"La division es: {Division()}\n\n")
    Operacion = Menu()

if Operacion == 5:
        print("Vuelva pronto")








