#list() crea una lista con los parametros dados, se puede usar para crear una lista sin elementos
#len cuenta la cantidad de elementos en la lista
#append agrega elemntos en la lista
lista=["hola",36, True]
lista.append("add")
print(lista)
#insert agrega un elemento en un indice especifico
lista.insert(0,"extendido")
print(lista)
#extend agrega varios elementos en la lista
lista.extend(["helado",33,2023,True])
print(lista)
#pop elimina el elemento del indice dado en la lista
lista.pop(3)
print(lista)
#si se coloca el indice -1 se borra el ultmo elemento de la lista

#remove remueve un elemento de la lista por su valor
lista.remove("hola")
print(lista)

#clear elimina todos los elementos de la lista
#lista.clear()

# sort ordena la lista de forma ascendente, no sirve si la lista tiene cadenas de texto
# lista.sort(reverse=True) de esta forma lo ordena en forma descendente

#reverse invierte los elemento de la lista
#lista.reverse()

