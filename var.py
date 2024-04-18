#desempaquetado de variables
#se puede asignar la informacion de una lista a varias variables
datos=("Jose","rosales", 64)
nombre, apellido, ci=datos
print(nombre)
#solo funciona si la cantidad de variables es igual a la cantidad de datos
#tambien se pueden crear tuplas sin los parentesis
#si se quiere crear una tupla con un solo dato se le coloca al final una coma
tupla="dato1",
#la funcion frozenset permite crear un conjunto inmutable que se puede colocar dentro de otro conjunto
conjunto=frozenset(["hola","adios"])
#la funcion issubset sirve para saber si un conjunto es un subconjunto de otro
conjunto1={1,2,3,4,5,6,7}
conjunto2={1,3,5,7}
resultado=conjunto2.issubset(conjunto1)
print(resultado)
#tambien se puede verificar con el <=
#para verificar si es un superconjunto se usa issuperset
resultado=conjunto1.issuperset(conjunto2)
print(resultado)
#la funcion isdisjoint devuelve true si en los conjuntos no hay ningun valor en comun
resultado=conjunto1.isdisjoint(conjunto2)
