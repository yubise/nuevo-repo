def numeros_primos(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True
def cant_primos(num):
    for x in range(2,num+1):
        if numeros_primos(x):
            print(x)
num=int(input("ingrese un numero: "))
cant_primos(num)
