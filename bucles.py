# los elementos iterables son las listas, tuplas,strings, diccionarios,conjuntos
#para iterar listas con for se usa una variable y como rango se coloca la lista
dragon_ball=["goku","vegeta",'nappa','krilin','gohan']

for x in dragon_ball:
    print(x)
#iterar dos listas juntas, deben tener la misma cantidad de elementos
    
numeros={12,23,34,45,56}
for personaje,numero in zip(dragon_ball,numeros):
    print(personaje,numero)
#funciona con mas de dos listas
#otra forma de recorrer la lista
for num,i in enumerate(dragon_ball):
    print(num)
    print(i)
#tambien se puede
for x in enumerate(numeros):
    print(x)
#en este caso crea una tupla
#se puede usar el else en un bucle y se muestra una vez al final del bucle
for x in range(2):
    print("hola")
    break
else:
    print("se acabó")
#cuando se usa break no muestra el else

