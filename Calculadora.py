##################################################################
#   Crear una aplicacion que implemente: suma, resta, multiplicacion y division de n numeros.
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
        print(f"Ingreso una letra\n")

def Suma(n):
    SumaTotal = 0
    for i in range(0,n):
        SumaTotal = SumaTotal + int(input(f"Ingrese {i+1} numero: \n"))
    return SumaTotal
    
######  Principal   ######
print("Sumas, resta, multiplicacion y division de n numeros:")   #Titulo del programa

#validacion
Operacion = Menu()

while Operacion > 5 and Operacion < 0:
    try:
        print("Muy bien")
    except ValueError:
        print("Llamaste una letra ingresar un numero del 1 al 5..")
    else:
        n = int(input("Ingrese cantidad de numeros a operar: "))    #Ingreso de la cantidad de numeros a operar
        if Operacion == 1:
            print(f"La suma es: {Suma(n)}")

'''


#restricciones
#try 
#except
#finally

def dividir(num,div):
  return num/div


try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    num=int(input("numero 1: "))
    div=int(input("numero 2: "))
    res=dividir(num/div)
    
    
except ZeroDivisionError:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    print("Trataste de dividir entre cero")

except ValueError:
    print("llamastes una letra ...")

else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
    print(res)
   
finally:
	# Este bloque se ejecutara siempre
    print("gracias")
'''