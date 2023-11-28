
diccionario = {}
'''Escribir un programa que permita gestionar la base de datos del alumnado
 de una clase. Los alumnos y alumnas se guardarán en un diccionario donde la
clave será el nombre del alumno y el valor será un valor booleano donde se almacenará 
si el alumno ha aprobado o suspendido. El programa debe preguntar al usuario por una opción 
del siguiente menú: (1) Añadir alumno/a, (2) Número de aprobados, (3) Mostrar todo el alumnado
 En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del alumno/a (nombre, aprobado/suspendido, añadir al diccionario los datos.
Obtener el número de aprobados con el siguiente formato: ‘El número de aprobados es: XX’.
Mostrar toda la clase.
'''
print("Opción 1 : Añadir alumno/a. Opción 2 : Número de aprobados"
      "Opción 3 : Mostrar todos los alumnos")

alumnos = input("Elige una opción ").lower()

if alumnos == "1":
    agregar = input("Añadir alumn/o: ")
    aprobado = input("Escribe True (aprobado) o False (reprobado)").capitalize()
if aprobado == "True":
    diccionario[agregar] = aprobado
else:
    diccionario[agregar] = aprobado

lista = []
if alumnos == "2":
    lista.append(diccionario.values)

    print(lista)

    


# print(diccionario)