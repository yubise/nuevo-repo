#type permite saber que tipo de dato es una variable
c=type(5)
print(c)

for x in range(1,10):
    if x<5:
        print(x)
    else:
        print(10-x)

#en un condicional para usar el else if se escribe elif
#metodos de cadenas: DIR, UPPER,LOWER,CAPITALIZE
#dir muestra todo lo que se puede hacer
#Upper coloca todo en mayuscula
#Lower coloca todo en minuscula
#Capitalize coloca la primera letra en mayuscula y lo demas en minuscula
print("hola mundo".upper())
#find busca un valor que le pidamos
bus="esternocleidomastoideo".find("e")
print(bus)
#devuelve la posicion en la que se encuentre lo que se pide
#devuelve -1 cuando no encuentra el dato que se busca
#index funciona igual excepto que lanza una excepcion si no encuentra nada
#isnumeric devuelve true si es numerico
#isalpha devuelve true si es alphanumerico es decir las letras de a hasta z
#count dice cuantas veces se encontro una coincidencia al valor buscado
bus="esternocleidomastoideo".count("o")
print(bus)
#len permite contar cuantos caracteres tiene una cadena
bus=len("hipopotomonstruosesquipedaliofobia")
print(bus)
#startswith verifica si una cadena empieza con otra dada
bus="hipopotomonstruosesquipedaliofobia".startswith("hipo")
print(bus)
#endswith verifica si la cadena termina en otra cadena dada

#replace reemplaza un pedazo de la cadena dada por una nueva

bus="esternocleidomastoideo".replace("deo","diosa")
print(bus)
#si no encuentra el valor solicitado no hara el reemplazo

#split separa cadenas con la cadena que se le pase

bus="hola cama juega mona capa".split(" ")
print(bus)
#crea una lista con los valores que se separan
