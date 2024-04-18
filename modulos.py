#los modulos son cualquier archivo .py
# desde un modulo se puede llamar a otro y crearlo
#hay tres tipos de modulos
#los creados por python que ya estan incluidos
#estan los modulos de terceros creados por personas que se pueden descargar
# modulos propios creados por nosotros


# se puede usar as para llamar de otra manera al modulo importado
#import prueba_modulo as mo
#print(mo.saludar("bebe"))


#tambien se puede importar unicamente la funcion

from prueba_modulo import saludar
print(saludar("bb"))
