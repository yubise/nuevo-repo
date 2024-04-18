def obcom(cantidad):
    compas=[]
    for i in range(cantidad):
        nombre=input("ingrese el nombre del alumno: ")
        edad=int(input("ingrese la edad del alumno: "))
        compa=(nombre,edad)
        compas.append(compa)
    compas.sort(key=lambda x:x[1])
    maestro=compas[-1][0]
    asistente=compas[0][0]
    return maestro,asistente
cant=int(input("ingrese cantidad de compañeros: "))
maestro,asistente=obcom(cant)
print("el maestro es ",maestro," y el asistente es ",asistente) 

