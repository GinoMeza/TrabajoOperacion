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