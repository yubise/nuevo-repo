dic={
    "nombre":"jose",
    "apellido":"rosales",
    "edad":22
}

#keys muestra las llaves del diccionario
print(dic.keys())

#get se le pone de parametro una key y devuelve le valor que guarda

print(dic.get("edad"))

#clear elimina todos los elementos

#pop elimina un elemento
dic.pop("edad")
print(dic)

