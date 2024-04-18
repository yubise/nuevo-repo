#lambda permite crear una funcion anomima
cubo= lambda x: x**3
print(cubo(3))
#funcion filter muestra los valores que son true de una lista, el true depende de la condicion dada
#la condicion puede ser una funcion lambda
num=[1,2,3,4,5,6,7,8,9]
pares=filter(lambda numero:numero%2 == 0, num)
print(list(pares))
