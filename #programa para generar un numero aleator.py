#programa para generar un numero aleatorio en pythom
import random
a= input("limite inferior:")
b= input("limite superior:")
#la funcion input captura datos desde el teclado, como si fuera un string (cadena de texto)

#convertir a enteror

a=int(a)
b=int(b)

respuesta = random.randint(a,b)
print("tu numero es",respuesta)