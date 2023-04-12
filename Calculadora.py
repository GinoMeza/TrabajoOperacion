##################################################################
#   Crear una aplicacion que implemente: suma, resta, multiplicacion y division de numeros.
#   Validar los numeros por parametros para los numeros



def Menu():
    Opc = 0
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    try:
        Opc = int(input(f"Ingrese opcion: \n"))
        while(Opc < 1 or Opc > 5):
            Opc = int(input(f"ERROR! Opcion solo 1 a 5, ingrese nuevamente: \n"))
        return Opc
    except ValueError:
        print(F"\nERROR!!   Ingreso una letra, el programa se cerrara.")

def Suma(n):                        #Funcion encargada de la suma
    SumaTotal = 0
    try:
        for i in range(0,n):            #Usamos for para repetir las "n" veces
            SumaTotal = SumaTotal + int(input(f"Ingrese {i+1} numero: \n"))
    except ValueError:
        print(F"\nERROR!!   Ingreso una letra, el programa se reiniciara.")
    return SumaTotal                #Devolver la suma
    
def Resta(n):                       #Funcion encargada de la resta
    Diferencia = 0
    try:
        for i in range(0,n):            #Usamos for para repetir las "n" veces
            Diferencia = Diferencia - int(input(f"Ingrese {i+1} numero: \n"))
    except ValueError:
        print(F"\nERROR!!   Ingreso una letra, el programa se reiniciara.")
    return Diferencia               #Devolver la diferencia

def Multiplicacion(n):              #Funcion encargada 
    Producto = 0
    try:
        for i in range(0,n):
            Producto = Producto * int(input(f"Ingrese {i+1} numero: \n"))
    except ValueError:
        print(F"\nERROR!!   Ingreso una letra, el programa se reiniciara.")
    return Producto

def Division():
    try:
        Dividendo = int(input(f"Ingrese dividendo: \n"))
        Divisor = int(input(f"Ingrese divisor(diferente a 0):\n"))
    except ValueError:
        print(F"\nERROR!!   Ingreso una letra, el programa se reiniciara.")
    
    try:
        Cociente = Dividendo/Divisor
    except ZeroDivisionError:
        print(f"Ingreso un numero cero, ingrese nuevamente:\n")
    else:
        return Cociente
    


######  Principal   ######
print(f"********            Sumas, resta y multiplicacion de n numeros y division de 2 numeros           **********\n\n")   #Titulo del programa

#validacion

Operacion = Menu()
if Operacion != 4:
    n = int(input(f"\nIngrese cantidad de numeros a operar(Suma, resta, multiplicacion): \n"))    #Ingreso de la cantidad de numeros a operar


while Operacion != 5:
    try:   
        if Operacion == 1:
            print(f"La suma es: {Suma(n)}\n\n")
        elif Operacion == 2:
            print(f"La resta es: {Resta(n)}\n\n")
        elif Operacion == 3:
            print(f"La multiplicacion es: {Multiplicacion(n)}\n\n")
        elif Operacion == 4:
            print(f"La division es: {Division()}\n\n")
    except ValueError:
        print("ingresaste una letra........")
    finally:
        Operacion = Menu()


if Operacion == 5:
        print("Vuelva pronto")







