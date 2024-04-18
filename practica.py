frase=input("ingresa un texto: ")
palabras=frase.count(" ")+1
tiempo= palabras /2
print(palabras)
if tiempo>60:
    print("para flaco tampoco es un testamento")
print("una persona tardaría ",tiempo," segundos en decirlo")
dalto=tiempo*7/10
print("dalto lo diria en "+str(dalto)+" segundos")

