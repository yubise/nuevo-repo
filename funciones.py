#funiones max() y min() devuelven el numero mas alto y el mas bajo
numeros = [1,4,7,-2]
print(max(numeros))
print(min(numeros))
#funcion round redondea un numero, su primer parametro es el numero
#el segundo parametro es el numero de decimales
print(round(13.241245531231,3))
#all() devuelve false si alguno de los valores dentro es 0 o vacio
#creando funciones
def saludar():
    print("hello word")

saludar()
# funciones con retorno de valores
def calculo(numero):
    car="abcdefghij"
    num_en=str(numero)
    num_en=int(num_en[0])
    c1=num_en-2
    c2=num_en
    c3=num_en-4
    con=car[c1]+car[c2]+car[c3]+str(num_en*2)
    return con
clave=calculo(363)
print(clave)
#para retornar valores se usa return
def suma(x):
    if x<10:
        suma(x+1)
        print(x)
suma(0)
def sume(*numeros):
    return sum(numeros)
a=sume(1,2,3,4,5,6,7,8,9)
print(a)
#el * es un parametro args que convierte todos los valores colocados en una lista
#para usarlo debe se rel ultimo parametro a colocar
